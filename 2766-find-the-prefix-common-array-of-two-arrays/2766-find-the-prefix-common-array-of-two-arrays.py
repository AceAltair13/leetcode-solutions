class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        freq = defaultdict(int)
        counter = 0
        ans = [0] * len(A)

        for i in range(len(A)):
            a, b = A[i], B[i]
            freq[a] += 1
            freq[b] += 1

            if a == b:
                counter += 1
            else:
                if freq[a] % 2 == 0:
                    counter += 1
                if freq[b] % 2 == 0:
                    counter += 1
            
            ans[i] = counter
        
        return ans