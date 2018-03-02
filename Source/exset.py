from Source.node import Node

class Explored:
    exset = []

    def __init__(self, a):
        self.exset = a

    def print_n(self):
        print("Explored", self.exset)

    def check(self,a):
        if a in self.exset:
            return True
        else:
            return False

    def add(self,a):
        self.exset.append(a)

