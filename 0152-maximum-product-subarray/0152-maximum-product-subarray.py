class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prod_1, prod_2, result = nums[0], nums[0], nums[0]
        
        for x in nums[1:]:
            temp = max(x, prod_1 * x, prod_2 * x)
            prod_2 = min(x, prod_1 * x, prod_2 * x)
            prod_1 = temp

            result = max(prod_1, result)
        
        return max(result, prod_1)