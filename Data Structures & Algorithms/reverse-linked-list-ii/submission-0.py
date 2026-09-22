class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)

        # fast will become the node at right + 1
        fast = head
        for _ in range(right - left + 1):
            fast = fast.next

        # slow will become the node at left - 1
        slow = dummy
        for _ in range(left - 1):
            slow = slow.next
            fast = fast.next

        # Save the first node of the section
        start = slow.next

        # Reverse [left, right]
        pre = slow
        curr = slow.next

        while curr != fast:
            temp = curr.next
            curr.next = pre
            pre = curr
            curr = temp

        # Reconnect
        slow.next = pre
        start.next = fast

        return dummy.next