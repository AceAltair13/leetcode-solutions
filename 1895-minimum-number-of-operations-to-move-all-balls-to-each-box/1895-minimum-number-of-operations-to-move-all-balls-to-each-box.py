class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        answer = [0] * n
        
        moves = 0
        balls = 0
        for i in range(n):
            answer[i] += moves
            balls += int(boxes[i])
            moves += balls
        
        moves = 0
        balls = 0
        for i in range(n - 1, -1, -1):
            answer[i] += moves
            balls += int(boxes[i])
            moves += balls
        
        return answer
