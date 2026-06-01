"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_mapping = {}

        # create Node objects
        curr = head
        while curr:
            copy_node = Node(curr.val)
            node_mapping[curr] = copy_node
            curr = curr.next
        node_mapping[None] = None
        
        # Link all the copy Nodes
        curr = head
        dummy = node_mapping[head]
        while curr:
            node_mapping[curr].next = node_mapping[curr.next]
            node_mapping[curr].random = node_mapping[curr.random]
            curr = curr.next

        return dummy