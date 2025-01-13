class Solution:
    def minimumLength(self, s: str) -> int:
        count_s = Counter(s)
        str_len = 0

        for v in count_s.values():
            if v > 2:
                x = 2 if v % 2 == 0 else 1
                str_len += x
            else:
                str_len += v
        
        return str_len