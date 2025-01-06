class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)
        
        while len(heap) > 1:
            diff = abs(heapq.heappop(heap) - heapq.heappop(heap))
            if diff:
                heapq.heappush(heap, -diff)
        
        return abs(heap[0]) if heap else 0