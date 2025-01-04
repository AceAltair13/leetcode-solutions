class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        N = sum(nums)
        if N % 2 != 0:
            return False
        
        N //= 2
        dp = set()
        dp.add(0)

        for i in range(len(nums)):
            next_dp = set()
            for x in dp:
                next_dp.add(x + nums[i])
                next_dp.add(x)
            dp = next_dp
        
        return True if N in dp else False
        


