# Kattis's Quest
N = int(input())

# [[G, G, G], [G, G, G]]
quests = [[] for _ in range(10**5)]


class Node:
    def __init__(self, energy, gold):
        self.energy = energy
        self.gold = [gold]

        self.left = None
        self.right = None

    def add_quest(self, energy, gold):
        if energy == self.energy:
            i = 0
            while i < len(self.gold) and self.gold[i] > gold:
                i += 1
            self.gold.insert(i, gold)
        elif energy > self.energy:
            if self.right is None:
                self.right = Node(energy, gold)
            else:
                self.right.add_quest(energy, gold)
        else:
            if self.left is None:
                self.right = Node(energy, gold)
            else:
                self.right.add_quest(energy, gold)

    def get_quest(self, max_energy):
        energy = 0
        if self.right is not None:
            energy = self.right.get_quest(max_energy)
            if energy:
                return energy, gold
        if self.energy == max_energy and self.gold != []:
            return self.energy, self.gold.pop(0)

    def remove_quest(self, energy):
        if self.energy < energy:
            return self.right.remove_quest()



root = None

for _ in range(N):
    line = input().split()
    if line[0] == "add":
        E = int(line[1])
        G = int(line[2])
        if root is None:
            root = Node(E, G)
        else:
            root.add_quest(E, G)
    else:
        X = int(line[1])
        G = 0
        i = X - 1
        while X > 0 and i > -1:
            if quests[i] != [] and X - 1 >= i:
                G += quests[i].pop(0)
                X -= i + 1
                i = X - 1
            else:
                i -= 1
        print(G)
