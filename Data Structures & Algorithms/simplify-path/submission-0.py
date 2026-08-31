class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        result = []
        stack = deque()
        print(path)
        
        for f in path:
            # Ignore extra slash or "."
            if not f or f == ".":
                continue
            
            if f == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(f)
            
        return "/" + "/".join(stack)
