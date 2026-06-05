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
            for _ in range(len(stack_p)):
                node_p = stack_p.popleft()
                node_q = stack_q.popleft()

                if not node_p and not node_q:
                    continue
                if not node_p or not node_q or node_p.val != node_q.val:
                    return False
                stack_p.append(node_p.left)
                stack_p.append(node_p.right)

                stack_q.append(node_q.left)
                stack_q.append(node_q.right)
        return True
