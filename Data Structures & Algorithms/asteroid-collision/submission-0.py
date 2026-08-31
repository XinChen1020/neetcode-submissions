class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            if not stack:
                stack.append(a)
                continue
            while stack and a < 0 and stack[-1] > 0:

                # Collision only happens if the top is moving right (+)
                # when the incoming one is moving left (-)
                    
                if abs(a) > stack[-1]:
                    stack.pop()
                elif abs(a) == stack[-1]:
                    a = 0
                    stack.pop()
                    break
                else:
                    a = 0
                    break

            if a:
                stack.append(a)
        return stack


