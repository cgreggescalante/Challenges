# Su Doku

class Cell:
    def __init__(self, n):
        n = int(n)
        if n > 0:
            self.value = n
        else:
            self.value = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def eliminate(self, n):
        if type(self.value) == list:
            for i in n:
                try:
                    self.value.remove(i)
                except ValueError:
                    continue
            self.complete()

    def complete(self, n=None):
        if type(self.value) == list:
            if len(self.value) == 1:
                self.value = self.value[0]
            elif n:
                self.value = n
        return type(self.value) == int

    def __str__(self):
        if type(self.value) == int:
            return str(self.value)
        else:
            return "[" + ' '.join([str(a) for a in self.value]) + "]"


class Board:
    def __init__(self, initial):
        self.board = []
        for a in initial:
            self.board.append([Cell(i) for i in a.strip()])

    def solve(self):
        i = 0
        while not self.complete() and i < 100:
            self.eliminate()
            i += 1

        if i == 100:
            for x in range(9):
                print(' '.join([str(a) for a in self.board[x]]))
        else:
            return int(''.join(str(a.value) for a in self.board[0][:3]))

    def eliminate(self):
        # ROWS
        for i in range(9):
            self.sector(self.board[i])

        # COLUMNS
        for i in range(9):
            self.sector([self.board[j][i] for j in range(9)])

        # SECTORS
        for i in range(3):
            for j in range(3):
                arr = []
                for io in range(3):
                    arr.extend([self.board[i*3+io][j*3+jo] for jo in range(3)])
                self.sector(arr)

    def sector(self, arr):
        eff = True
        while eff:
            eff = False
            cmpl = [a.value for a in arr if a.complete()]
            for a in arr:
                if a.eliminate(cmpl):
                    eff = True
                a.complete()

        missing = []
        for a in arr:
            if not a.complete():
                missing.extend(a.value)

        for m in missing:
            if m in [a.value for a in arr]:
                missing.remove(m)

        unique = [a for a in missing if missing.count(a) == 1]

        for u in unique:
            for a in arr:
                if not a.complete():
                    if u in a.value:
                        a.complete(u)

    def complete(self):
        return all(all(type(self.board[i][j].value) == int for i in range(9)) for j in range(9))


with open("C:\\Users\\Conor\\PycharmProjects\\EulerStuff\\Resources\\Sudoku96.txt", "r") as file:
    lines = file.readlines()

    while len(lines) > 0:
        print(lines.pop(0).strip())
        B = Board(lines[:9])
        print(B.solve())
        lines = lines[9:]
