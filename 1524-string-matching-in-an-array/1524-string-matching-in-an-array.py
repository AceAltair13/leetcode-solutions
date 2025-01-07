class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        mega_string = ",".join(words)
        ans = []
        
        for word in words:
            if mega_string.count(word) > 1:
                ans.append(word)
        
        return ans