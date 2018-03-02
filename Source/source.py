from agent import Agent

agent = Agent(3, 3)
answer = agent.search()
if answer is not None:
    print("Answer: ")
    answer.print_p()
else:
    print("No solution")
