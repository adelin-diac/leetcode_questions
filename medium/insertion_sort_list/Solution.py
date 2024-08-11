from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None

        sorted_head = ListNode(0)
        tmp = head

        while tmp:
            next_node = tmp.next
            # tmp is the current node we're on
            # every node before is sorted
            # go from the start until you find a node
            # bigger than current one - insert before it
            prev = sorted_head
            while prev.next and prev.next.val < tmp.val:
                prev = prev.next
            
            # insert between the previous one and the next one (when found the value more than current one)
            tmp.next = prev.next
            prev.next = tmp

            tmp = next_node
        return sorted_head.next
