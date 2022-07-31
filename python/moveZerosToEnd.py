"""
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
"""


def move_zeros(lst):
    zeros = 0
    while 0 in lst:
        lst.remove(0)
        zeros += 1
    for _ in range(0, zeros):
        lst.append(0)
    return lst


print(move_zeros([1, 0, 1, 2, 0, 1, 3]))
