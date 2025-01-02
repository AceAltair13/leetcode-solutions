class Solution:
    def romanToInt(self, s: str) -> int:
        _dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        ans = 0
        n = len(s)
        i = 0

        while i < n:
            if i < n - 1 and (
                (s[i] == "I" and s[i + 1] in ("V", "X"))
                or (s[i] == "X" and s[i + 1] in ("L", "C"))
                or (s[i] == "C" and s[i + 1] in ("D", "M"))
            ):
                ans += _dict[s[i + 1]] - _dict[s[i]]
                i += 2
            else:
                ans += _dict[s[i]]
                i += 1

        return ans
