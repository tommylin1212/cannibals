from exset import Explored
from frontier import Frontier
from node import Node


class Agent:
    def __init__(self, missionaries, cannibals):
        # actually turns out that with boat size 2, 3 pairs is the most
        self.missionaries = missionaries
        if self.missionaries < 3:
            self.missionaries = 3
        self.cannibals = cannibals
        if self.cannibals < 3:
            self.cannibals = 3
        self.front = Frontier([])
        self.explored_set = Explored([])
        self.start_node = Node(["L", missionaries, cannibals, 0, 0], None, "START")
        self.front.add(self.start_node)
        self.goal = Node(["R", 0, 0, missionaries, cannibals], None, "")

    @staticmethod
    def cmp(node1, node2):
        return (node1.state > node2.state) - (node1.state < node2.state)

    def get_legal(self, cur):
        moves = []
        if cur.state[0] == "L":
            if cur.state[1] > 0 and cur.state[2] > 0:
                moves.append(
                    Node(["R", cur.state[1] - 1, cur.state[2] - 1, cur.state[3] + 1, cur.state[4] + 1], cur, "MRCR"))
            if cur.state[2] > 0:
                moves.append(Node(["R", cur.state[1], cur.state[2] - 1, cur.state[3], cur.state[4] + 1], cur, "CR"))
            if cur.state[1] > 0:
                moves.append(Node(["R", cur.state[1] - 1, cur.state[2], cur.state[3] + 1, cur.state[4]], cur, "MR"))
            if cur.state[2] >= self.cannibals - 1:
                moves.append(Node(["R", cur.state[1], cur.state[2] - 2, cur.state[3], cur.state[4] + 2], cur, "CRCR"))
            if cur.state[1] >= self.missionaries - 1:
                moves.append(Node(["R", cur.state[1] - 2, cur.state[2], cur.state[3] + 2, cur.state[4]], cur, "MRMR"))

        else:
            if cur.state[3] > 0 and cur.state[4] > 0:
                moves.append(
                    Node(["L", cur.state[1] + 1, cur.state[2] + 1, cur.state[3] - 1, cur.state[4] - 1], cur, "MLCL"))
            if cur.state[4] > 0:
                moves.append(Node(["L", cur.state[1], cur.state[2] + 1, cur.state[3], cur.state[4] - 1], cur, "CL"))
            if cur.state[3] > 0:
                moves.append(Node(["L", cur.state[1] + 1, cur.state[2], cur.state[3] - 1, cur.state[4]], cur, "ML"))
            if cur.state[4] >= self.cannibals - 1:
                moves.append(Node(["L", cur.state[1], cur.state[2] + 2, cur.state[3], cur.state[4] - 2], cur, "CLCL"))
            if cur.state[3] >= self.missionaries - 1:
                moves.append(Node(["L", cur.state[1] + 2, cur.state[2], cur.state[3] - 2, cur.state[4]], cur, "MLML"))

        for node in moves:
            if node.state[1] != 0 and node.state[3] != 0:
                if node.state[1] < node.state[2] or node.state[3] < node.state[4]:
                    moves = [test_node for test_node in moves if self.cmp(test_node, node) != 0]

        return moves

    def search(self):
        # breadth first
        # will never have solution on first try
        while True:
            if len(self.front.frontier) == 0:
                return None
            next_node = self.front.front()
            self.explored_set.add(next_node)
            moves = self.get_legal(next_node)
            for node in moves:
                if not self.explored_set.check(node) and not self.front.check(node):
                    if self.cmp(node, self.goal) == 0:
                        return node
                    self.front.add(node)
