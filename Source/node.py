class Node:
	state = []
	parent = None
    

    def __init__(self, state, parent,action):
    	self.state = state
    	self.parent = parent
		self.action = action

    def print_n(self):
    	print("action: ",self.action,"-> state:", self.state)

    def print_p(self):
    	if self.parent is not None:
        	self.parent.print_p()
    	self.print_n()
