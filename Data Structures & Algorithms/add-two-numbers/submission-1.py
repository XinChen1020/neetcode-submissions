# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = curr = ListNode(0)
        plus_one = False

        while l1 or l2:

            if l1 and l2:
                result = l1.val + l2.val
            elif l1:
                result = l1.val
            else:
                result = l2.val

            if plus_one:
                result += 1
                plus_one = False

            if result >= 10:
                plus_one = True
                result = result % 10
            
            new_node = ListNode(result)
            curr.next = new_node
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        if plus_one:
            curr.next = ListNode(1)

        return dummy.next
