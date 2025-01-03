class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {nums[i]: i for i in range(len(nums))}
        for j in range(len(nums)):
            x = nums[j]
            if (target - x) in nums_dict and nums_dict[target - x] != j:
                return (j, nums_dict[target - x])
