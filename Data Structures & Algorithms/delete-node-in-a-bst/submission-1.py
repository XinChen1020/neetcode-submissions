class Solution:
    def deleteNode(
        self, root: Optional[TreeNode], key: int
    ) -> Optional[TreeNode]:

        parent = None
        curr_node = root

        # Find node
        while curr_node and curr_node.val != key:
            parent = curr_node

            if key > curr_node.val:
                curr_node = curr_node.right
            else:
                curr_node = curr_node.left

        if not curr_node:
            return root

        # Two children
        if curr_node.left and curr_node.right:
            # Promote the entire right subtree
            replacement = curr_node.right

            # Find smallest node in the right subtree
            successor = replacement
            while successor.left:
                successor = successor.left

            # Attach the original left subtree
            successor.left = curr_node.left

            # Deleting the root
            if not parent:
                return replacement

            if parent.left == curr_node:
                parent.left = replacement
            else:
                parent.right = replacement

        # One child
        elif curr_node.left or curr_node.right:
            child = curr_node.left if curr_node.left else curr_node.right

            if not parent:
                return child

            if parent.left == curr_node:
                parent.left = child
            else:
                parent.right = child

        # No children
        else:
            if not parent:
                return None

            if parent.left == curr_node:
                parent.left = None
            else:
                parent.right = None

        return root