class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        most_freq_count = max(freq.values())
        
        # Count of tasks with the max frequency
        max_count = sum(1 for x in freq.values() if x == most_freq_count)

        # Get the number of intervals
        intervals = (most_freq_count - 1) * (n + 1) + max_count
        
        # Return intervals
        return max(intervals, len(tasks))
