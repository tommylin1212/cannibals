class Node:
    state = []
    parent = None

    def __init__(self, a, p):
        self.state = a
        self.parent = p

    def print_n(self):
        print("state:", self.state)

    def print_p(self):
        if self.parent is not None:
            self.parent.print_p()
        self.print_n()
