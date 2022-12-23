# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 05:57:23 2022

@author: Charles

MIT study from textbook before 6.002x :-)

"""

class Item(object):
    def __init__(self, n, v, w):
        self._name = n
        self._value = v
        self._weight = w
        
    def get_name(self):
        return self._name
    def get_value(self):
        return self._value
    def get_weight(self):
        return self._weight
    def __str__(self):
        return f'<{self._name},\t{self._value},{self._weight}>'
    def value(item):
        return item.get_value()
    def weight_inverse(item):
        return 1.0 / item.get_weight
    def density(item):
        return item.get_value() / item.get_weight()
    
def greedy(items, max_weight, key_function):
    items_copy = sorted(items, key=key_function, reverse = True)
    result = []
    total_value, total_weight = 0.0, 0.0
    for i in range(len(items_copy)):
        if (total_weight + items_copy[i].get_weight()) <= max_weight:
            result.append(items_copy[i])
            total_weight += items_copy[i].get_weight()
            total_value += items_copy[i].get_value()
    return (result, total_value)

def build_items():
    names = ['printer', 'laptop', 'textbooks', 'camera', 'phone']
    values = [80, 1200, 100, 300, 600]
    weights = [5, 1.1, 20, 0.3, 0.1]
    Items = []
    for i in range(len(values)):
        Items.append(Item(names[i], values[i], weights[i]))
    return Items
    
def test_greedy(items, max_weight, key_function):
    taken, val = greedy(items, max_weight, key_function)
    print("Total value of items is", val)
    for item in taken:
        print('\t', item)
        
def test_greedys(max_weight = 5):
    items = build_items()
    print("Greedy by value")
    test_greedy(items, max_weight, Item.get_value)
    print("Greedy by weight")
    test_greedy(items, max_weight, Item.get_weight)
    print("Greedy by density")
    test_greedy(items, max_weight, Item.density)
    
if __name__ == "__main__": test_greedys()