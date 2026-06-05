# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Pre-order traversal is alwasy unique
        # Root -> Left -> Right
        def seralize(root: Optional[TreeNode]) -> str:
            stack = deque([root])
            s = ""
            while stack:
                node = stack.pop()

                if not node:
                    s += "#"
                    continue
                s += str(node.val)
                stack.append(node.left)
                stack.append(node.right)
            return s
        print(seralize(subRoot))
        print(seralize(root))
        return seralize(subRoot) in seralize(root)
