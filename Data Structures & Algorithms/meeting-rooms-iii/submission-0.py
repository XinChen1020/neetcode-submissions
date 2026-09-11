from _heapq import heappop
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        
        meetings.sort()

        # idx
        available = list(range(n))
        heapq.heapify(available)

        # min heap -> the earlist available room with the lowest index
        # (end time, room , heappushnumber)
        occupied = []

        result = [0] * n

        for idx, m in enumerate(meetings):
            start, end = m

            # Before processing current room, 
            # deteremin what's availbe and what's still occupied
            while occupied and start >= occupied[0][0]:
                _, room_number = heapq.heappop(occupied)
                heapq.heappush(available, room_number)
            
            # Start assign room for current meeting
            if available:
                room_number = heapq.heappop(available)
                heapq.heappush(occupied, [end, room_number])
            else:
                duration = end - start
                end_time, room_number = heapq.heappop(occupied)
                heapq.heappush(occupied, [end_time + duration, room_number]) 

            result[room_number] += 1

        return result.index(max(result))

                

            
            

