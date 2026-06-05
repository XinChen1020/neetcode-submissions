# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        node_mapping = {None: 0}

        stack = deque([root])

        while stack:
            node = stack[-1]

            if node.left and node.left not in node_mapping:
                stack.append(node.left)
            elif node.right and node.right not in node_mapping:
                stack.append(node.right)
            else:
                node = stack.pop()
                height = max(node_mapping[node.left], node_mapping[node.right])

                if abs(node_mapping[node.right] - node_mapping[node.left]) > 1:
                    return False
                
                node_mapping[node] = height + 1
        return True