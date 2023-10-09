"""
Module: search

Program that uses binary search to determine if a number is in a list.
"""

import random
from sys import argv, exit

def create_random_ordered_list(num_items: int) -> list[int]:
    """Generates an ordered list of integers of length <num_items>

    Precondition: num_items > 0

    Args:
        num_items (int): Number of items to generate for the list.

    Returns:
        list[int]: Random list or ordered integers
    """
    assert num_items > 0
    my_list = []
    prev = 0
    for _ in range(num_items):
        n = prev + random.randrange(2, 11)
        my_list.append(n)
        prev = n

    return my_list

def binary_search(nums: list[int], target: int) -> bool:
    """ Uses binary search to determine if <target> is in the ordered list <nums>,
    returning True if it is, and False otherwise. """

    first = 0
    last = len(nums) - 1

    while first <= last:
        midpoint = (first + last) // 2

        if nums[midpoint] == target:
            return True
        elif target < nums[midpoint]:
            last = midpoint - 1
        else:
            first = midpoint + 1

    return False


if __name__ == "__main__":
    # create and print random list of 5 ints
    my_nums = create_random_ordered_list(5)
    print("List:", my_nums)

    while True:
        choice = input("Enter an integer to search for: ")
        try:
            target = int(choice)
        except:
            print("Invalid entry. Try again!")
        
        else:
            found = binary_search(my_nums, target)
            if found:
                print(target, "was found!")
            else:
                print(target, "was NOT found!")
