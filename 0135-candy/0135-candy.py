class Solution:
    def candy(self, ratings: List[int]) -> int:
        # TC: O(N)
        # SC: O(N)

        n = len(ratings)
        candies = [1] * n
        
        # Left to right
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # Right to left
        for j in range(n - 2, -1, -1):
            if ratings[j] > ratings[j + 1]:
                candies[j] = max(candies[j + 1] + 1, candies[j])
        
        return sum(candies)