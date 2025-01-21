class Solution:
    def compress(self, chars: List[str]) -> int:
        read, write = 0, 0

        while read < len(chars):
            c = chars[read]
            count = 0

            while read < len(chars) and chars[read] == c:
                read += 1
                count += 1
            
            chars[write] = c
            write += 1
            if count > 1:
                for x in str(count):
                    chars[write] = x
                    write += 1
            
        return write