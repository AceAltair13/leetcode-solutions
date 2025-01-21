class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i = 0
        window_sum = sum(nums[i: i + k])
        max_avg = window_sum / k

        for i in range(len(nums) - k):
            window_sum -= nums[i]
            window_sum += nums[i + k]
            max_avg = max(max_avg, window_sum / k)
        
        return max_avg
            