class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        mod = len(s) % k
        divides = len(s) // k if mod == 0 else (len(s) // k) + 1
        ans = []
        i = 0
        
        for j in range(divides):
            ans.append(s[i: i + k])
            i += k
        
        if i == len(s):
            return ans
        
        ans[-1] = ans[-1] + (fill * (k - mod)) 

        return ans