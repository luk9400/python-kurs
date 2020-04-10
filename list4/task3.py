#!/usr/bin/python
from random import randint

NUMBER_OF_CHILDREN = 2

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def __str__(self):
        return str(self.value)


def generate_tree(node, height):
    if height == 0:
        return

    for _ in range(randint(1, NUMBER_OF_CHILDREN)):
        value = randint(0, 10)
        node.children.append(Node(value))

    for i in node.children:
        generate_tree(i, height - 1)

def bfs(node):
    queue = [node]

    while len(queue) > 0:
        node = queue.pop(0)

        yield node.value

        for i in node.children:
            queue.append(i)


def dfs(node):
    yield node.value
    for i in node.children:
        yield from dfs(i)

root = Node(0)
generate_tree(root, 3)
print(list(bfs(root)))
print(list(dfs(root)))