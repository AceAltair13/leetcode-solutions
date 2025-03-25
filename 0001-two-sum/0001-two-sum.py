class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # TC: O(N)
        # SC: O(N)
        
        num_dict = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in num_dict:
                return [i, num_dict[complement]]
            
            num_dict[num] = i
        
        return []