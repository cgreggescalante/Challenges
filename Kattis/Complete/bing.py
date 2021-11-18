# Bing It On

N = int(input())


class Node:
    def __init__(self, word):
        self.char = word[0]
        self.children = []
        self.count = 0
        self.add(word)

    def add(self, word):
        self.count += 1
        if len(word) == 1:
            return self.count - 1
        for child in self.children:
            if child.char == word[1]:
                return child.add(word[1:])
        self.children.append(Node(word[1:]))
        return 0


trees = []

for _ in range(N):
    word = input()
    found = False
    for tree in trees:
        if tree.char == word[0]:
            found = True
            print(tree.add(word))
    if not found:
        trees.append(Node(word))
        print(0)
