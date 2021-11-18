# Path sum: four ways
import heapq
from typing import List, Tuple, T


class PriorityQueue:
    def __init__(self):
        self.elements: List[Tuple[float, T]] = []

    def empty(self) -> bool:
        return not self.elements

    def put(self, item: T, priority: float):
        heapq.heappush(self.elements, (priority, item))

    def get(self) -> T:
        return heapq.heappop(self.elements)[1]


with open("../Resources/matrix82.txt") as file:
    matrix = []
    for line in file.readlines():
        matrix.append(list(map(int, line.split(","))))

start = (0, 0)
target = (len(matrix) - 1, len(matrix) - 1)

graph = {}
for i in range(len(matrix)):
    for j in range(len(matrix)):
        graph[(i, j)] = {"c": matrix[i][j], "n": []}
        neighbors = []
        if i > 0:
            neighbors.append((i - 1, j))
        if j > 0:
            neighbors.append((i, j - 1))
        if i < len(matrix) - 1:
            neighbors.append((i + 1, j))
        if j < len(matrix) - 1:
            neighbors.append((i, j + 1))
        graph[(i, j)]["n"] = neighbors


def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def a_star(graph, start, target):
    frontier = PriorityQueue()
    frontier.put(start, graph[start]["c"] + heuristic(start, target))
    came_from = {}
    current_cost = {}
    came_from[start] = None
    current_cost[start] = graph[start]["c"]

    while not frontier.empty():
        current = frontier.get()

        if current == target:
            break

        for next in graph[current]["n"]:
            new_cost = current_cost[current] + graph[next]["c"]
            if next not in current_cost or new_cost < current_cost[next]:
                current_cost[next] = new_cost
                priority = new_cost + heuristic(next, target)
                frontier.put(next, priority + graph[next]["c"])
                came_from[next] = current

    return came_from, current_cost


paths, costs = a_star(graph, start, target)

print(costs[target])
