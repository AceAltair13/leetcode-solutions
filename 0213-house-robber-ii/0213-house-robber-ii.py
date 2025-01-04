class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums)
            
        rob1, rob2 = 0, 0

        # [rob1, rob2, nums[1], nums[1] ... , nums[-1]]
        for x in nums[1:]:
            temp = max(rob1 + x, rob2)
            rob1, rob2 = rob2, temp
        
        # [_rob1, _rob2, nums[0], nums[1] ... , nums[-2]]
        _rob1, _rob2 = 0, 0
        for x in nums[:len(nums) - 1]:
            temp = max(_rob1 + x, _rob2)
            _rob1, _rob2 = _rob2, temp
        
        return max(rob2, _rob2)
