class Solution:
    def check(self, nums: List[int]) -> bool:
        violation = 0
        n = len(nums)

        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                violation += 1
                if violation > 1:
                    return False
        
        return True