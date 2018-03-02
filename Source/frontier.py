class Frontier:
    fron = []

    def __init__(self, a):
        self.fron = a

    def print_n(self):
        print("Explored", self.fron)

    def check(self, a):
        if a in self.fron:
            return True
        else:
            return False

    def add(self, a):
        self.fron.append(a)
