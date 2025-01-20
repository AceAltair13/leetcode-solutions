class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1 or nums[0] == 0:
            return 0
        
        jumps = 1
        steps, pointer = nums[0], nums[0]
        
        for i in range(1,len(nums)-1):
            steps -= 1
            pointer -= 1
            pointer = max(pointer,nums[i])
            
            if steps == 0:
                jumps += 1
                steps = pointer
        
        return jumps