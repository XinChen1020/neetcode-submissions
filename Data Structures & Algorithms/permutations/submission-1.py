class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        s = set()
        stack = deque([[s, []]])
        
        while stack:
            seen, curr_path = stack.pop()

            if len(curr_path) == len(nums):
                result.append(curr_path)
                continue
            
            for n in nums:
                if seen and n in seen:
                    continue
                s_c = seen.copy()
                s_c.add(n)
                stack.append([s_c, curr_path + [n]])
        return result