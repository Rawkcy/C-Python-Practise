#!/usr/env/python

"""
Sum multiples of 3 and 5 under 1000
"""

def return_sum(max_val):
    integers = []

    for i in range(1, max_val):
        if not i % 5 or not i % 3:
            integers.append(i)

    return sum(integers)

def comprehension_sum(max_val):
    return sum([i for i in range(1, max_val) if not i % 3 or not i % 5])

def get_range(enter, exit, limit):
    """
    Return the min and max of the people in the elevator

    min -> at least this many people in the beginning
    max -> at most this many people in the beginning
    """
    max_pop = min_pop = net_diff = 0
    for in,out in zip(enter, exit):
        net_diff += in - out
        if net_diff < min_pop:    min_pop = net_diff
        if net_diff > max_pop:    max_pop = net_diff
    #return { 0 - min_pop, limit - max_pop } if max_pop <= limit and min_pop >= 0 else {}
    return {}

