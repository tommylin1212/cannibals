class Frontier:
    frontier = []

    @staticmethod
    def cmp(state1, state2):
        return (state1 > state2) - (state1 < state2)

    def __init__(self, test_node):
        self.frontier = test_node

    def check(self, test_node):
        for node in self.frontier:
            if self.cmp(test_node.state, node.state) == 0:
                return True
        return False

    def add(self, test_node):
        self.frontier.append(test_node)

    def front(self):
        front_node = self.frontier[0]
        self.frontier = [test_node for test_node in self.frontier if self.cmp(test_node.state, front_node.state) != 0]
        return front_node

    def print_n(self):
        print("Frontier: ")
        for node in self.frontier:
            node.print_n()
