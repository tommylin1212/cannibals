class Node:
    state = []
    parent = None

    def __init__(self, state, parent):
        self.state = state
        self.parent = parent

    def print_n(self):
        print("state:", self.state)

    def print_p(self):
        if self.parent is not None:
            self.parent.print_p()
        self.print_n()
