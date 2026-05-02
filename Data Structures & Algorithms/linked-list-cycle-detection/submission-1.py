# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Hash
        """seen = set()
        cur = head
        while cur:
            if cur in seen:
                return True
            seen.add(cur)
            cur = cur.next
        return False"""
        # Pointers
        first, second = head, head
        while second and second.next:
            first = first.next
            second = second.next.next
            if first == second:
                return True
        return False