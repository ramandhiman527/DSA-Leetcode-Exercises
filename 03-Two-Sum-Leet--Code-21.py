# -*- coding: utf-8 -*-
"""03 LeetCode 1. Two Sum.ipynb

## **Two Sum**

"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for i, num in enumerate(nums):
            if num in d:
                return [d[num], i]
            else:
                d[target - num] = i
