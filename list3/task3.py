def sum_last_column(filename):
    with open(filename, 'r') as f:
        return sum(int(line.split()[-1]) for line in f.readlines())


print(sum_last_column('./test.txt'))
