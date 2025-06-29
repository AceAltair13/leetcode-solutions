class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        start_candidate = 0
        tank = 0
        
        for i in range(len(gas)):
            tank_diff = gas[i] - cost[i]
            tank += tank_diff

            if tank < 0:
                start_candidate = i + 1
                tank = 0

        return start_candidate