class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        heap = []
        result = []

        for i in range(len(tasks)):
            tasks[i].append(i)

        tasks.sort()

        curr_time = 0
        i = 0

        while len(result) < len(tasks):

            # If CPU is idle, jump to the next available task
            if not heap and curr_time < tasks[i][0]:
                curr_time = tasks[i][0]

            # Add every task that has become available
            while i < len(tasks) and tasks[i][0] <= curr_time:
                enqueue, processing, idx = tasks[i]
                heapq.heappush(heap, (processing, idx))
                i += 1

            processing, idx = heapq.heappop(heap)
            result.append(idx)
            curr_time += processing

        return result