class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        num_boat = 0

        # max heap
        # keep boat with most room at the top
        prev_room = []

        for i in range(len(people) - 1, -1, -1):

            if not prev_room or people[i] > -prev_room[0]:
                num_boat += 1
                
                if limit - people[i] > 0:
                    heapq.heappush(prev_room, -(limit - people[i]))
            else:
                heapq.heappop(prev_room)
    

        return num_boat