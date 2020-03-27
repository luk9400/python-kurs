def elts_lt_x(x, l):
    return list(filter(lambda y: y < x, l))


def elts_qreq_x(x, l):
    return list(filter(lambda y: y >= x, l))


def quicksort(l):
    if l == []:
        return []

    return quicksort(elts_lt_x(l[0], l[1:])) + [l[0]] + quicksort(elts_qreq_x(l[0], l[1:]))


print(quicksort([4, 2, 1, 7, 8, 6]))
