class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        alt = False
        text = ""
        n1, n2 = len(word1), len(word2)

        i, j = 0, 0

        while i < n1 and j < n2:
            if alt:
                text += word2[j]
                j += 1
                alt = False
            else:
                text += word1[i]
                i += 1
                alt = True
        
        if i < n1:
            text += word1[i:]
        elif j < n2:
            text += word2[j:]

        return text
            