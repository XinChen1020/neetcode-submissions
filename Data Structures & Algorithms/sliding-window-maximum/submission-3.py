class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # mono queue
        mono_q = deque()
        result = []
        for i in range(len(nums)):

            while mono_q and nums[i] > mono_q[-1][0]:
                mono_q.pop()
            mono_q.append((nums[i], i))
            while mono_q and mono_q[0][1] < i - k + 1:
                mono_q.popleft()
            if i >= k - 1:
                result.append(mono_q[0][0])
        return result
            