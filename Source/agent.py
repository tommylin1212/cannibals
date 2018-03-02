from Source.node import Node
from Source.exset import Explored
from Source.frontier import Frontier


class Agent:
    def __init__(self, a):
        self.front = Frontier([])
        self.exset = Explored([])
        self.cur = Node([0, 3, 3, 0, 0])
        self.front.add(self.cur)

    def getLegal(self, a):
        if a[0]==1:
            temp = Node([1, a[1] - 1, a[2] - 1, a[3] + 1, a[4] + 1]) #1 of each go right

        else:

