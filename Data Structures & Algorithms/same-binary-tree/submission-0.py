# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # BFS
        stack_p = deque([p])
        stack_q = deque([q])

        while stack_p:
            node_p = stack_p.popleft()
            node_q = stack_q.popleft()

            if node_p and not node_q:
                return False
            if node_q and not node_p:
                return False
            if node_p and node_q:
                if node_p.val != node_q.val:
                    return False
                stack_p.append(node_p.left)
                stack_p.append(node_p.right)

                stack_q.append(node_q.left)
                stack_q.append(node_q.right)
        return True
