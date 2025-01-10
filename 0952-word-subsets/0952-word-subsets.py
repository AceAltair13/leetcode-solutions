class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        max_freq = Counter()
        for b in words2:
            b_count = Counter(b)
            for char in b_count:
                if b_count[char] > max_freq[char]:
                    max_freq[char] = b_count[char]

        universal_words = []
        for a in words1:
            a_count = Counter(a)
            is_universal = True
            for char in max_freq:
                if a_count.get(char, 0) < max_freq[char]:
                    is_universal = False
                    break
            if is_universal:
                universal_words.append(a)

        return universal_words
