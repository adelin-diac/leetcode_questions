# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        current = dummy

        while list1 and list2:
            if list1.val >= list2.val:
                current.next = list2
                list2 = list2.next
            else:
                current.next = list1
                list1 = list1.next
            current = current.next
        if list1:
            current.next = list1
        if list2:
            current.next = list2

        return dummy.next

print(Solution().mergeTwoLists(ListNode(2, ListNode(3, ListNode(5))), ListNode(4)))