class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def gcd(a, b):
            if a == 0:
                return b
            return gcd(b % a, a)

        _gcd = gcd(len(str1), len(str2))

        prefix = str1[:_gcd]

        if (
            prefix * (len(str1) // _gcd) == str1
            and prefix * (len(str2) // _gcd) == str2
        ):
            return prefix

        return ""
