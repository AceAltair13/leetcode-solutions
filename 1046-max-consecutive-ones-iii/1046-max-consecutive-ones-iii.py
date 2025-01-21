class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i, zeroes, window = 0, 0, 0

        for j in range(len(nums)):
            if nums[j] == 0:
                zeroes += 1
            while zeroes > k:
                if nums[i] == 0:
                    zeroes -= 1
                i += 1
            w = j - i + 1
            window = max(window, w)
        
        return window
                
