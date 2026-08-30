class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # Greedy
        # Always place the heaviest plus the lightest (if not over limit) on the boat

        # O(NlogN)
        people.sort()
        result = 0
        l, r = 0, len(people) - 1
        while l <= r:
            result += 1

            if people[l] + people[r] <= limit:
                l += 1
            r -= 1

        return result
