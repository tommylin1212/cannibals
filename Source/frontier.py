class Frontier:
    fron = []

    @staticmethod
    def cmp(a, b):
        return (a > b) - (a < b)

    def __init__(self, a):
        self.fron = a

    def check(self, a):
        for node in self.fron:
            if self.cmp(a.state, node.state) == 0:
                return True
        return False

    def add(self, a):
        self.fron.append(a)

    def front(self):
        x = self.fron[0]
        self.fron = [n for n in self.fron if self.cmp(n.state, x.state) != 0]
        return x

    def print_n(self):
        print("Frontier: ")
        for node in self.fron:
            node.print_n()
