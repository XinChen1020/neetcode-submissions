class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        location = {}
        for i in range(len(nums1)):
            location[nums1[i]] = i
        
        result = [-1] * len(nums1)

        # Monotonic decreasing stack
        # store val
        stack = deque()

        for i in range(len(nums2)):
            while stack and stack[-1] < nums2[i]:
                val = stack.pop()
                if val in location:
                    result[location[val]] = nums2[i]
            
            stack.append(nums2[i])
        
        return result

        