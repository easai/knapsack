""" pytest files for knapsack.sort()
"""
from src.knapsack.knapsack import *
import pytest

dirt = Item(4, 0, 'dirt')
computer = Item(10, 30, 'computer')
fork = Item(5, 1, 'fork')
ps = Item(0, -10, 'ps')

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
    res = k.sort(knapsack.min_weight)
    assert res[0] == ps


def test_max_value():
    """Test max value
    """
    res = k.sort(knapsack.max_value)
    assert res[0] == computer
