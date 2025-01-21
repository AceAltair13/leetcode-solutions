class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans = [False] * len(candies)
        max_candies = max(candies)

        for i, c in enumerate(candies):
            if c + extraCandies >= max_candies:
                ans[i] = True
        
        return ans