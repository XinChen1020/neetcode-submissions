class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        task_freq = Counter(tasks)

        # We don't need to know the letter, just need to know there's
        # a unique task available 
        task_available_heap = [-v for _ , v in task_freq.items()]
        heapq.heapify(task_available_heap)

        cooldown_queue = deque()

        while task_available_heap or cooldown_queue:
            time += 1

            # one task may become available again
            if cooldown_queue and time - cooldown_queue[0][0] > n:
                _, neg_freq = cooldown_queue.popleft()
                heapq.heappush(task_available_heap, neg_freq)

            if task_available_heap:
                neg_freq = heapq.heappop(task_available_heap)
                neg_freq += 1

                if neg_freq < 0:
                    cooldown_queue.append((time, neg_freq))

        return time