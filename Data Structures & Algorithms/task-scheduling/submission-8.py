class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Greedy
        task_freq_count = Counter(tasks)
        k, max_freq = task_freq_count.most_common(1)[0]
        task_freq_count.pop(k)
        idle_slots = (max_freq - 1) * n

        # Fill each idle slots in between
        for _, v in task_freq_count.items():
            idle_slots -= min(max_freq - 1, v)
        
        # If there's more tasks than available idle slots,
        # there's always a way to align them such that there's no
        # idel time
        return max(0, idle_slots) + len(tasks)