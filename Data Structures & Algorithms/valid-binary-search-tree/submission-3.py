# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # DFS -> get max of left and right subtree
        # node: (min, max)
        min_max_node = {None: (1001, -1001)}
        stack = deque([root])

        while stack:
            node = stack[-1]

            if not node:
                continue

            if node.left and node.left not in min_max_node:
                stack.append(node.left)
            elif node.right and node.right not in min_max_node:
                stack.append(node.right)
            else:
                node = stack.pop()
                if node.left and min_max_node[node.left][1] >= node.val:
                    return False
                if node.right and min_max_node[node.right][0] <= node.val:
                    return False
                min_max_node[node] =  (min(min_max_node[node.left][0], node.val), max(min_max_node[node.right][1], node.val))
        return True
        