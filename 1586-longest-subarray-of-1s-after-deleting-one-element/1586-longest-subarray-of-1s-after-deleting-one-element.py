class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l, zeroes = 0, 0
        max_window = 0

        for r in range(len(nums)):

            if nums[r] == 0:
                zeroes += 1
            
            while zeroes > 1:
                if nums[l] == 0:
                    zeroes -= 1
                l += 1
            
            max_window = max(max_window, r - l + 1)
        
        return max_window - 1