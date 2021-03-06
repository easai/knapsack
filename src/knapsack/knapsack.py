"""An implementation of Knapsack problem solver

This is knapsack.py
"""
import math
import copy


class Item():
    """Class for an object.

    This is a class for an object that will be packed into the knapsack.
    An object has a label that identify the object,
    weight the total of which limits the capacity of the knapsack,
    value the total of which should be maximized.

    Attributes:
        weight (int): the weight of the object
        value (int): the value of the object
        label (str): the label of the object

    """

    def __init__(self, weight, value, label):
        """Constructor.

        Args:
            weight (int): the weight of the object
            value (int): the value of the object
            label (str): the label of the object
        """
        self.weight = weight
        self.value = value
        self.label = label

    def get_value(self):
        """Return the value of the object.

        Returns:
            int: the value of the object
        """
        return self.value

    def get_weight(self):
        """Return the weight of the object.

        Returns:
            int: the weight of the object
        """
        return self.weight

    def dump(self):
        """Print the label, weight, and value of the object
        """
        print(f"[{self.label}] w={self.weight} val={self.value}")


class knapsack():
    """Class for list of Item objects

    This class represents a list of item class.
    The packing algorithms should be implmented as methods of this class.

    Attributes:
        itemlist (list): the list of Item objects
    """

    def __init__(self, itemlist):
        """Constructor.

        Args:
            itemlist (list): a list of Item objects
        """
        self.itemlist = itemlist

    def set_list(self, lst):
        """Set the itemlist.

        Args:
            itemlist (list): a list of Item objects
        """
        self.itemlist = lst

    def get_list(self):
        """Get the itemlist.

        Returns:
            itemlist (list): a list of Item objects
        """
        return self.itemlist

    def dump(self):
        """Print each object.
        """
        for item in self.itemlist:
            item.dump()

    def sort(self, f):
        """Sort the list in the order specified function.

        Args:
            f (function): the key function for sorting

        Returns:
            list: the sorted list of items
        """
        return sorted(self.itemlist, key=f, reverse=True)

    def run(self, f, maxWeight=14):
        """Print the packed items sorted by the specified functions.

        Args:
            f (function): this is the function whose return value ranks the order of selection
            maxWeight (:obj:`int`, optional): maximum capacity of the knapsack
        """
        totalWeight = 0
        lst = copy.copy(self.itemlist)
        while lst and totalWeight < maxWeight:
            item = get_max(lst, f)
            totalWeight += item.get_weight()
            if 14 < totalWeight:
                break
            item.dump()
            lst.remove(item)

    @staticmethod
    def ratio(item):
        """Return value/weight ratio.

        Args:
            item (item): the item class object
        """
        v = item.get_value()
        if item.get_weight() != 0:
            res = v / item.get_weight()
        else:
            if v < 0:
                res = -math.inf
            elif v == 0:
                res = 0
            else:
                res = math.inf
        return res

    @staticmethod
    def min_weight(item):
        """Return the -weight (-1 x weight) of the item class object.

        Args:
            item (item): the item class object
        """
        return -item.get_weight()

    @staticmethod
    def max_value(item):
        """Return the value of the item class object.

        Args:
            item (item): the item class object
        """
        return item.get_value()


def get_max(lst, f):
    """Return the max item class object by the specified function.

    Args:
        lst (list): the list of item
        f (function): the function
    """
    if lst:
        val = f(lst[0])
    else:
        return None
    res = lst[0]
    for item in lst:
        v = f(item)
        if val < v:
            val = v
            res = item
    return res
