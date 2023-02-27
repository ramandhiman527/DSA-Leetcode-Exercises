# -*- coding: utf-8 -*-
"""01-Contains-Duplicate--LeetCode-Problem-217.ipynb

#### **Solution Using Set**

    Time Complexity --> O(n) as set uses only O(1) and we are iterating array only once.
"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_set = set()
        for num in nums:
            if num in num_set:
                return True
            else:
                num_set.add(num)
        return False

"""#### **Solution using Sorting Method**"""

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_set = set()
        for num in nums:
            if num in num_set:
                return True
            else:
                num_set.add(num)
        return False