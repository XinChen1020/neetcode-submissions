# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        # Both slow and dummy reference to the same object at the begining
        slow, fast = dummy, head

        for _ in range(n):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        print(dummy.next)
        return dummy.next