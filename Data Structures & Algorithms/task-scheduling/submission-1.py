class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        task_freq = Counter(tasks)
        task_freq_heap = [(-v, k) for k, v in task_freq.items()]
        heapq.heapify(task_freq_heap)

        queue = deque()

        while task_freq_heap or queue:
            time += 1

            # one task may become available again
            if queue and time - queue[0][0] > n:
                _, neg_freq, letter = queue.popleft()
                heapq.heappush(task_freq_heap, (neg_freq, letter))

            if task_freq_heap:
                neg_freq, letter = heapq.heappop(task_freq_heap)
                neg_freq += 1

                if neg_freq < 0:
                    queue.append((time, neg_freq, letter))

        return time