class Solution:
    def grayCode(self, n: int) -> List[int]:
        # TC: O(2^N)
        # SC: O(2^N)

        ans = [0]

        for i in range(n):
            ans += [x | 1 << i for x in reversed(ans)]
        
        return ans