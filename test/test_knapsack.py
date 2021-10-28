from src.knapsack.knapsack import *
import pytest

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


def test_ratio():
    print("--- [value/weight]")
    k.run(knapsack.ratio)
    print()


def test_min_weight():
    k.setList([dirt, computer, fork, ps])
    print("--- [-weight]")
    k.run(knapsack.minWeight)
    print()


def test_max_value():
    k.setList(lst)
    print("--- [value]")
    k.run(knapsack.maxValue)
    print()
