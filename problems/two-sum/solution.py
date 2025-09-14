import json
import sys
from typing import List


"""
Given an array of integers nums and an integer target,
return indices of the two numbers
such that they add up to target. You may assume that each
input would have exactly one solution,
and you may not use the same element twice.
You can return the answer in any order.

"""


def two_sum(nums: List[int], target: int) -> List[int]:
    # implement your solution here
    pass


if __name__ == "__main__":
    test_case = json.load(open(sys.argv[1], 'r'))
    result = two_sum(*test_case['args'])
    if '--output' in sys.argv:
        print(json.dumps(result))
    else:
        sys.exit(0 if result == test_case['expected'] else 1)
