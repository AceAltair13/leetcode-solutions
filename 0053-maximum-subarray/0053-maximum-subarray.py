class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        _sum = 0
        for x in nums:
            _sum = max(_sum + x, x)
            max_sum = max(_sum, max_sum)
        return max_sum