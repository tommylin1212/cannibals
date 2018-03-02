from agent import Agent

agent = Agent()
answer = agent.search()
if answer is not None:
    print("Answer: ")
    answer.print_p()
else:
    print("No solution")
