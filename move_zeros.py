
from typing import Iterable

def move_zeros(items: list) -> Iterable[int]:
    """
    You are given a list of integers. Move all zeros in the list to the end of it. The order of non-zero elements should not change.
    """
    return [x for x in items if x != 0] + [x for x in items if x == 0]

print(move_zeros([0]))


assert list(move_zeros([0, 1, 0, 3, 12])) == [1, 3, 12, 0, 0]
assert list(move_zeros([0])) == [0]