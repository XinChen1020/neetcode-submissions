class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        # Two pointer, pair heaviest with the lighlist
        
        people.sort()
        num_boat = 0
        l, r = 0, len(people) - 1
        while l <= r:
            num_boat += 1
            if people[l] + people[r] <= limit:
                l += 1

            r -= 1

        return num_boat