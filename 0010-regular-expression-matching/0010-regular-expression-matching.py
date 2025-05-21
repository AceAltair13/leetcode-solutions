class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        def dp_solve(s_idx, p_idx):
            if (s_idx, p_idx) in memo:
                return memo[(s_idx, p_idx)]
            
            if p_idx == len(p):
                result = (s_idx == len(s))
                memo[(s_idx, p_idx)] = result
                return result
            
            first_char_match = (s_idx < len(s) and (p[p_idx] == s[s_idx] or p[p_idx] == "."))

            if p_idx + 1 < len(p) and p[p_idx + 1] == "*":
                match_if_star_is_zero = dp_solve(s_idx, p_idx + 2)
                match_if_star_is_one_or_more = False
                
                if first_char_match:
                    match_if_star_is_one_or_more = dp_solve(s_idx + 1, p_idx)

                result = match_if_star_is_zero or match_if_star_is_one_or_more

            else:
                if first_char_match:
                    result = dp_solve(s_idx + 1, p_idx + 1)
                else:
                    return False
            
            memo[(s_idx, p_idx)] = result
            
            return result
        
        return dp_solve(0, 0)