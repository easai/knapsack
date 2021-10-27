from knapsack import *


clock = item(10, 175, 'clock')
picture = item(9, 90, 'picture')
radio = item(4, 20, 'radio')
vase = item(2, 50, 'vase')
book = item(1, 10, 'book')
computer = item(20, 200, 'computer')

lst = [clock, picture, radio, vase, book, computer]
k = knapsack(lst)
print("items in the knapsack")
k.dump()
print()

print("--- [Max value]")
k.setList(lst)
k.run(maxValue, 20)
print()
std = k.sort(maxValue)
res = knapsack(std)
res.dump()
print()

print("--- [Min weight]")
k.setList(lst)
k.run(minWeight, 20)
print()
std = k.sort(minWeight)
res = knapsack(std)
res.dump()
print()


print("--- [value/weight]")
k.setList(lst)
k.run(ratio, 20)
print()
std = k.sort(ratio)
res = knapsack(std)
res.dump()
print()
