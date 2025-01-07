class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort()
        ans = set()
        
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j:
                    pattern, word = words[i], words[j]
                    if pattern in word:
                        ans.add(pattern)
        
        return list(ans)
