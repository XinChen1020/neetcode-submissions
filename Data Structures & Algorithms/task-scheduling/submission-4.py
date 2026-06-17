class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        task_freq = Counter(tasks)

        # We don't need to know the letter, just need to know there's
        # a unique task available 
        task_available_heap = [-v for v in task_freq.values()]
        heapq.heapify(task_available_heap)

        cooldown_queue = deque()

        while task_available_heap or cooldown_queue:
            time += 1

            if task_available_heap:
                neg_freq = heapq.heappop(task_available_heap)
                neg_freq += 1

                if neg_freq < 0:
                    cooldown_queue.append((time, neg_freq))
            else:
                # Since there's no more task to assign,
                # we can fast progress the counter to when
                # we WILL have a task by adding the closet one to finish cool down
                time = cooldown_queue[0][0] + n

            # one task may become available again and push back into heap
            if cooldown_queue and time - cooldown_queue[0][0] >= n:
                heapq.heappush(task_available_heap, cooldown_queue.popleft()[1])


        return time