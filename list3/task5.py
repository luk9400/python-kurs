def allsubsets(s):
    if s == []:
        return [[]]

    return list(map(lambda b: [s[0]] + b, allsubsets(s[1:]))) + allsubsets(s[1:])


print(allsubsets([1, 2, 3]))
