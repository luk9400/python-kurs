matrix = ["1.1 2.2 3.3", "4.4 5.5 6.6", "7.7 8.8 9.9"]


def transpose(matrix):
    return [" ".join(row.split()[i] for row in matrix) for i in range(len(matrix))]


print(transpose(matrix))
