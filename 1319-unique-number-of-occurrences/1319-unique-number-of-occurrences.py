class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        unique = set()

        for v in counter.values():
            unique.add(v)
        
        return len(unique) == len(counter.values())