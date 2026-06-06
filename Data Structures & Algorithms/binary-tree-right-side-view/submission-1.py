# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # BFS -> right most node of each level
        if not root:
            return []
        queue = deque([root])
        result = [root.val]
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()

                if node:
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            if queue:
                result.append(queue[-1].val)
            
        return result