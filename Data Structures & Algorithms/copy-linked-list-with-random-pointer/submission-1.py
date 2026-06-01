"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
from collections import defaultdict
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_mapping = defaultdict(lambda: Node(0))
        node_mapping[None] = None

        # create Node objects
        curr = head
        while curr:
            node_mapping[curr].val = curr.val
            node_mapping[curr].next = node_mapping[curr.next]
            node_mapping[curr].random = node_mapping[curr.random]
            curr = curr.next

        return node_mapping[head]