class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()   # stores indices
        result = []

        for r in range(len(nums)):
            # Remove smaller elements from the back
            while q and nums[q[-1]] <= nums[r]:
                q.pop()

            q.append(r)

            # Remove elements outside the window
            if q[0] <= r - k:
                q.popleft()

            # Window is ready
            if r >= k - 1:
                result.append(nums[q[0]])

        return result