# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head
        slow, fast = None, head

        while fast:
            # Save next processing node
            temp = fast.next
            
            # Reverse
            fast.next = slow

            # Progress both pointer
            slow = fast
            fast = temp
        
        return dummy, slow

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Go k steps (slow, fast)
        # Reverse them

        # Dummy to cover edge case and used for returning result
        dummy = slow = fast = ListNode()
        dummy.next = head
        count = k

        while True:
            while fast:
                fast = fast.next
                count -= 1
                if not fast or count == 0:
                    break
            if not fast:
                break
            temp = fast.next
            fast.next = None
            reverse_head, reverse_tail = self.reverseList(slow.next)
            slow.next =  reverse_tail
            reverse_head.next = temp

            fast = slow = reverse_head
            count = k
            
            
        return dummy.next

