
class Explored:
    explored_set = []

    @staticmethod
    def cmp(state1, state2):
        return (state1 > state2) - (state1 < state2)

    def __init__(self, test_node):
        self.explored_set = test_node

    def print_n(self):
        print("Explored: ")
        for node in self.explored_set:
            node.print_n()

    def check(self, test_node):
        for node in self.explored_set:
            if self.cmp(test_node.state, node.state) == 0:
                return True
        return False

    def add(self, test_node):
        self.explored_set.append(test_node)
