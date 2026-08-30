class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # the weight capacity must be at least the max weights
        # otherwise, can't carry
        # the highest weight capacity could be the sum of the weights
        # carry everything in one days
        # Binary search between [max(weights), sum(weights)]
        # find the leftmost boundary, such that the task can be completed in days
        # If the

        # Check if the task can be completed >= days
        def valid(capacity: int) -> bool:
            days_req = 0
            curr_weight = 0
            for i in range(len(weights)):
                if curr_weight + weights[i] > capacity:
                    days_req += 1
                    curr_weight = weights[i]
                else:
                    curr_weight += weights[i]
            days_req += 1

            return days_req <= days
        l, r = max(weights), sum(weights)
        while l <= r:
            # avoid overflow
            mid = (r - l) // 2 + l

            if valid(mid):
                r = mid - 1
            else:
                l = mid + 1
        
        return l