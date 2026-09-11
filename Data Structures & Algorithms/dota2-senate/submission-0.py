class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
        R_queue = deque()
        Q_queue = deque()

        for i in range(len(senate)):
            if senate[i] == "R":
                R_queue.append(i)
            else:
                Q_queue.append(i)

        offset = len(senate)
        while R_queue and Q_queue:
            if R_queue[0] < Q_queue[0]:
                idx = R_queue.popleft()
                Q_queue.popleft()
                # For looping
                R_queue.append(offset + idx)
            else:
                idx = Q_queue.popleft()
                R_queue.popleft()
                Q_queue.append(offset + idx)
        
        if len(Q_queue) == 0:
            return "Radiant"
        else:
            return "Dire"
