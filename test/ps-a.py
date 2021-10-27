from knapsack import *


dirt=item(4,0,'dirt')
computer=item(10,30,'computer')
fork=item(5,1,'fork')
ps=item(0,-10,'ps')

lst=[dirt,computer,fork,ps]

#getMax(lst,metric1).dump()
#getMax(lst,metric2).dump()
#getMax(lst,metric3).dump()

lst=[dirt,computer,fork,ps]
k=knapsack(lst)
print("items in the knapsack")
k.dump()
print()

print("--- [value/weight]")
k.run(metric1)
print()
k.setList([dirt,computer,fork,ps])
print("--- [-weight]")
k.run(metric2)
print()
k.setList(lst)
print("--- [value]")
k.run(metric3)
print()


