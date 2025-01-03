class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        heap = []

        for _k, _v in freq.items():
            if len(heap) < k:
                heapq.heappush(heap, (_v, _k))
            else:
                heapq.heappushpop(heap, (_v, _k))

        return [x[1] for x in heap]
        
