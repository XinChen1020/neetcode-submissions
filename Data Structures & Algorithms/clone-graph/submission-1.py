"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        # bfs
        if not node:
            return None
        node_mapping = defaultdict(lambda: Node(0))
        node_mapping[node].val = node.val
        queue = deque([node])
        while queue:

            for _ in range(len(queue)):
                curr_node: Node = queue.popleft()
                neighbors = []
                for n in curr_node.neighbors:
                    if n not in node_mapping:
                        queue.append(n)

                    # defaultdict creates the node and then assign value
                    node_mapping[n].val = n.val
                    neighbors.append(node_mapping[n])
                         
                node_mapping[curr_node].neighbors = neighbors

        return node_mapping[node]