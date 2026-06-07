# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    # BFS
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "N"
        queue = deque([root])
        result = []
        while queue:
            node = queue.popleft()
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result += "N"
        return ".".join(result)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = data.split(".")
        if data[0] == "N":
            return None
        root = TreeNode(int(data[0]))
        queue = deque([root])
        idx = 1
        while queue:
            node = queue.popleft()
            if data[idx] != "N":
                node.left = TreeNode(int(data[idx]))
                queue.append(node.left)
            idx += 1
            if data[idx] != "N":
                node.right = TreeNode(int(data[idx]))
                queue.append(node.right)
            idx += 1
        return root
