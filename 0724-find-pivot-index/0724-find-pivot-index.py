class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = [0] * len(nums)
        right = [0] * len(nums)

        for i in range(1, len(nums)):
            left[i] = nums[i - 1] + left[i - 1]
        
        for j in range(len(nums) - 2, -1, -1):
            right[j] = nums[j + 1] + right[j + 1]

        for k in range(len(nums)):
            if left[k] == right[k]:
                return k
        
        return -1