# -*- coding: utf-8 -*-
"""05 || Merge-Two-Sorted-Lists || LeetCode-21 || .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15PZK1J1lYUpVysICiXMyNp4HNI9gEFYe

Link to the question -- 

    [https://leetcode.com/problems/merge-two-sorted-lists/submissions/]

***The solution uses a dummy node and two pointers, one for each input list.***

***We compare the values of the nodes pointed to by the two pointers and append the smaller one to the result list.***

This process continues until we reach the end of one of the input lists. 

***Finally, we append the remaining nodes of the non-empty list to the result list.***

***The result list is returned after skipping the initial dummy node.***
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy        

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        elif list2: