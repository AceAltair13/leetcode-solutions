class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant = deque()
        dire = deque()
        n = len(senate)

        for i, s in enumerate(senate):
            if s == "R":
                radiant.append(i)
            else:
                dire.append(i)

        while radiant and dire:
            i, j = radiant.popleft(), dire.popleft()

            if i < j:
                radiant.append(i + n)
            else:
                dire.append(j + n)
        
        return "Radiant" if radiant else "Dire"