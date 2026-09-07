from functools import cache

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        @cache
        def dfs(node):
            if not node:
                return 0

            # Option 1: don't rob this node
            skip = dfs(node.left) + dfs(node.right)

            # Option 2: rob this node
            # Then we cannot rob its children,
            # so move directly to the grandchildren.
            rob = node.val

            if node.left:
                rob += dfs(node.left.left) + dfs(node.left.right)

            if node.right:
                rob += dfs(node.right.left) + dfs(node.right.right)

            return max(rob, skip)

        return dfs(root)