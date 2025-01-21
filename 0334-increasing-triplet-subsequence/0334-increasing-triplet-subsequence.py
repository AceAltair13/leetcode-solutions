class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first, second = float('inf'), float('inf')

        for x in nums:
            if x < first:
                first = x
            elif first < x < second:
                second = x
            elif x > second:
                return True
        
        return False