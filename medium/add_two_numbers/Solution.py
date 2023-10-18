# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def length(self):
        temp = self.val
        count = 0

        while temp:
            count += 1
            temp = temp.next
        
        return count
    
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
      # initilaise first one as 0 (this will be skipped at the end)
      dummy = ListNode() # [{val: 0, next: None}]
      current = dummy
      carry = 0

      # end of this while loop will change these to None when needed
      while l1 or l2 or carry:
          
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        total = val1 + val2 + carry

        carry = total // 10 # should only ever be 0 or 1

        current.next = ListNode(total % 10)

        # move pointer to next element so it can continue moving along
        current = current.next

        if l1:
           l1 = l1.next # basically removing first node from linked list
        if l2:
           l2 = l2.next
          
      return dummy.next
          
        

l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))

solution = Solution().addTwoNumbers(l1, l2)
print(solution)