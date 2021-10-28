""" pytest files for knapsack.sort()
"""
from src.knapsack.knapsack import *
import pytest

dirt = item(4, 0, 'dirt')
computer = item(10, 30, 'computer')
fork = item(5, 1, 'fork')
ps = item(0, -10, 'ps')

lst = [dirt, computer, fork, ps]
k = knapsack(lst)


def test_ratio():
    """Test ratio (value/weight)
    """
    res = k.sort(knapsack.ratio)
    assert res[0] == computer


def test_min_weight():
    """Test min min
    """
    res = k.sort(knapsack.minWeight)
    assert res[0] == ps


def test_max_value():
    """Test max value
    """
    res = k.sort(knapsack.maxValue)
    assert res[0] == computer
