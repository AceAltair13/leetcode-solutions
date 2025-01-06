class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            dist = point[0] ** 2 + point[1] ** 2
            heapq.heappush(heap, (dist, point))
        ans = []
        while k > 0:
            ans.append(heapq.heappop(heap)[1])
            k -= 1
        return ans
