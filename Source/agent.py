from Source.exset import Explored
from Source.frontier import Frontier
from Source.node import Node


class Agent:
    def __init__(self):
        self.front = Frontier([])
        self.exset = Explored([])
        self.cur = Node(["L", 3, 3, 0, 0], None)
        self.front.add(self.cur)
        self.goal = Node(["R", 0, 0, 3, 3], None)

    @staticmethod
    def cmp(a, b):
        return (a.state > b.state) - (a.state < b.state)

    def get_legal(self, a):
        rle = []
        if a.state[0] == "L":
            if a.state[1] > 0 and a.state[2] > 0:
                rle.append(Node(["R", a.state[1] - 1, a.state[2] - 1, a.state[3] + 1, a.state[4] + 1], a))
            if a.state[2] > 0:
                rle.append(Node(["R", a.state[1], a.state[2] - 1, a.state[3], a.state[4] + 1], a))
            if a.state[1] > 0:
                rle.append(Node(["R", a.state[1] - 1, a.state[2], a.state[3] + 1, a.state[4]], a))
            if a.state[2] >= 2:
                rle.append(Node(["R", a.state[1], a.state[2] - 2, a.state[3], a.state[4] + 2], a))
            if a.state[1] >= 2:
                rle.append(Node(["R", a.state[1] - 2, a.state[2], a.state[3] + 2, a.state[4]], a))

        else:
            if a.state[3] > 0 and a.state[4] > 0:
                rle.append(Node(["L", a.state[1] + 1, a.state[2] + 1, a.state[3] - 1, a.state[4] - 1], a))
            if a.state[4] > 0:
                rle.append(Node(["L", a.state[1], a.state[2] + 1, a.state[3], a.state[4] - 1], a))
            if a.state[3] > 0:
                rle.append(Node(["L", a.state[1] + 1, a.state[2], a.state[3] - 1, a.state[4]], a))
            if a.state[4] >= 2:
                rle.append(Node(["L", a.state[1], a.state[2] + 2, a.state[3], a.state[4] - 2], a))
            if a.state[3] >= 2:
                rle.append(Node(["L", a.state[1] + 2, a.state[2], a.state[3] - 2, a.state[4]], a))

        for node in rle:
            if node.state[1] != 0 and node.state[3] != 0:
                if node.state[1] < node.state[2] or node.state[3] < node.state[4]:
                    rle = [n for n in rle if self.cmp(n, node) != 0]

        return rle

    def search(self):
        # will never have solution on first try
        while True:
            if len(self.front.fron) == 0:
                return None
            nextn = self.front.front()
            self.exset.add(nextn)
            self.exset.print_n()
            self.front.print_n()
            moves = self.get_legal(nextn)
            print("Current:")
            nextn.print_n()
            print("Neighbors: ")
            for node in moves:
                node.print_n()
            for node in moves:
                if not self.exset.check(node) and not self.front.check(node):
                    if self.cmp(node, self.goal) == 0:
                        return node
                    self.front.add(node)
