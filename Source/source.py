from Source.agent import Agent

a = Agent()
answer = a.search()
if answer is not None:
    print("Answer: ")
    answer.print_p()
else:
    print("No solution")
