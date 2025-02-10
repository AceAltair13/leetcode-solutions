class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        number = 0
        curr_str = ""

        for x in s:
            if x.isdigit():
                number = number * 10 + int(x)
            elif x == "[":
                stack.append((curr_str, number))
                curr_str, number = "", 0
            elif x == "]":
                last_str, repeat_count = stack.pop()
                curr_str = last_str + curr_str * repeat_count
            else:
                curr_str += x
        
        return curr_str