#!/usr/bin/python

from random import randint, random


def generate_tree(height):
    if height == 0:
        return None

    proper_tree = generate_tree(height - 1)
    random_tree = generate_tree(randint(0, height - 1))

    val = randint(0, 10)

    if random() > 0.5:
        return [str(val), proper_tree, random_tree]
    else:
        return [str(val), random_tree, proper_tree]


def dfs(tree):
    if tree is not None:
        yield from dfs(tree[1])
        yield tree[0]
        yield from dfs(tree[2])


def bfs(tree):
    queue = [tree]

    while len(queue) > 0:
        node = queue.pop(0)

        yield node[0]

        if node[1] is not None:
            queue.append(node[1])
        if node[2] is not None:
            queue.append(node[2])


tree = generate_tree(3)
print(tree)

print(list(dfs(tree)))
print(list(bfs(tree)))
