

class Explored:
    exset = []

    @staticmethod
    def cmp(a, b):
        return (a > b) - (a < b)

    def __init__(self, a):
        self.exset = a

    def print_n(self):
        print("Explored: ")
        for node in self.exset:
            node.print_n()

    def check(self, a):
        for node in self.exset:
            if self.cmp(a.state, node.state) == 0:
                return True
        return False

    def add(self, a):
        self.exset.append(a)
