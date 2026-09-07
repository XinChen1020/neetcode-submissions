from functools import cache

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        @cache
        def dfs(node):
            if not node:
                # Rob, not rob
                return 0, 0
                
            left_rob, left_skip = dfs(node.left)
            right_rob, right_skip = dfs(node.right)

            # Option 1: don't rob this node
            skip = max(left_rob, left_skip) + max(right_rob, right_skip)

            # Option 2: rob this node
            rob = node.val
            rob += left_skip + right_skip

            return rob, skip

        return max(dfs(root))