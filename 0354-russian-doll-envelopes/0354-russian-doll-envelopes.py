class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        heights = [x for _, x in envelopes]
        tails = []

        for h in heights:
            idx = bisect_left(tails, h)
            
            if idx == len(tails):
                tails.append(h)
            else:
                tails[idx] = h

        return len(tails)
        