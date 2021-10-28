from src.knapsack.knapsack import *
import pytest

clock = item(10, 175, 'clock')
picture = item(9, 90, 'picture')
radio = item(4, 20, 'radio')
vase = item(2, 50, 'vase')
book = item(1, 10, 'book')
computer = item(20, 200, 'computer')

lst = [clock, picture, radio, vase, book, computer]
k = knapsack(lst)


def test_max_value():
    """Max value test
    """
    res = k.sort(knapsack.maxValue)
    assert res[0] == computer


def test_min_weight():
    """Min weight test
    """
    res = k.sort(knapsack.minWeight)
    assert res[0] == book


def test_ratio():
    """Ratio value/weight test
    """
    res = k.sort(knapsack.ratio)
    assert res[0] == vase
