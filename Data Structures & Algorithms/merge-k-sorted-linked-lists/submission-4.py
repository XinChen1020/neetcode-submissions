# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        heapq.heapify(heap)

        # Use this to break tie since ListNode has no way to compare
        # and heapq will compare ListNode if we only use (l.val,l)
        count = 0

        for l in lists:
            while l:
                heapq.heappush(heap, (l.val, count, l))
                count += 1
                l = l.next
        
        dummy = curr = ListNode()

        while heap:
            node = heapq.heappop(heap)[2]
            curr.next = node
            curr = node
            

        return dummy.next

        