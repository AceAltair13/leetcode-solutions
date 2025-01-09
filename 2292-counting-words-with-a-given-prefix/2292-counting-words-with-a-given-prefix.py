class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        words = [word[:len(pref)] for word in words]
        return sum(1 for word in words if word == pref)