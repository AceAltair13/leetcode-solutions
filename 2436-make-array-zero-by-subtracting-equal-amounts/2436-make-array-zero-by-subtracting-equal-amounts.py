class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        _nums = set(nums)
        if 0 in _nums:
            _nums.remove(0)
        
        return len(_nums)