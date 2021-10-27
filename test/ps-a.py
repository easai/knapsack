from knapsack import *


dirt = item(4, 0, 'dirt')
computer = item(10, 30, 'computer')
fork = item(5, 1, 'fork')
ps = item(0, -10, 'ps')

lst = [dirt, computer, fork, ps]

lst = [dirt, computer, fork, ps]
k = knapsack(lst)
print("items in the knapsack")
k.dump()
print()

print("--- [value/weight]")
k.run(ratio)
print()
k.setList([dirt, computer, fork, ps])
print("--- [-weight]")
k.run(minWeight)
print()
k.setList(lst)
print("--- [value]")
k.run(maxValue)
print()
