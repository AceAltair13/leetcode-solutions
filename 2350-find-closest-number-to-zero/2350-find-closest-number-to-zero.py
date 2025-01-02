class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        ans = float("inf")

        for x in nums:
            temp_ans, temp_x = abs(ans), abs(x)
            if temp_ans > temp_x:
                ans = x
            elif temp_ans == temp_x:
                ans = max(ans, x)
        
        return ans