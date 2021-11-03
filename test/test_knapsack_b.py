""" pytest files for knapsack.sort()
"""
from src.knapsack.knapsack import *
import pytest

clock = Item(10, 175, 'clock')
picture = Item(9, 90, 'picture')
radio = Item(4, 20, 'radio')
vase = Item(2, 50, 'vase')
book = Item(1, 10, 'book')
computer = Item(20, 200, 'computer')

lst = [clock, picture, radio, vase, book, computer]
k = knapsack(lst)


def test_max_value():
    """Max value test
    """
    res = k.sort(knapsack.max_value)
    assert res[0] == computer


def test_min_weight():
    """Min weight test
    """
    res = k.sort(knapsack.min_weight)
    assert res[0] == book


def test_ratio():
    """Ratio value/weight test
    """
    res = k.sort(knapsack.ratio)
    assert res[0] == vase
