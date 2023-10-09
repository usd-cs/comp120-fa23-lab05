"""
Module: exceptional

A simple module to demonstrate exceptions.
"""

def foo(n: int) -> int:
    return 100 // n

def get_max(filename: str) -> int:
    """ Finds the largest amount in a CSV file where each line contains
    a name and an amount"""

    with open(filename, 'r') as f:
        f.readline()
        for line in f:
            cols = line.strip().split(',')
            amount = int(cols[1])
            if amount > largest:
                largest = amount

    return largest
