import hashlib
import os
import sys

def info_crawler(path, file_info={}):
    for dirpath, dirnames, filenames in os.walk(path):
        for file in filenames:
            key = ''
            if dirpath == './':
                key = dirpath + file
            else:
                key = dirpath + '/' + file
            
            file_info[key] = {
                "size": os.path.getsize(dirpath + '/' + file),
                "hash": file_hash(dirpath + '/' + file),
                "checked": False
            }

        for subdir in dirnames:
            info_crawler(dirpath + subdir, file_info)

    return file_info


def repchecker(path):
    file_info = info_crawler(path)

    for file in file_info:
        file_info[file]['checked'] = True
        found_copy = False
        for file2 in file_info:
            if not file_info[file2]['checked'] and file_info[file]['size'] == file_info[file2]['size'] and  file_info[file]['hash'] == file_info[file2]['hash']:
                file_info[file2]['checked'] = True
                found_copy = True
                print(file2)
        if found_copy == True:
            print(file)
            print('-------------------------')


def file_hash(path):
    with open(path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


if __name__ == '__main__':
    path = sys.argv[1]
    repchecker(path)