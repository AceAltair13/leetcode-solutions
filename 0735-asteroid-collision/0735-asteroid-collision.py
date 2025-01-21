class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for x in asteroids:

            while stack and x < 0 < stack[-1]:

                if abs(x) > stack[-1]:
                    # Asteroids destroys top of stack
                    stack.pop()
                    continue
                elif abs(x) == stack[-1]:
                    # Both asteroids destroy each other
                    stack.pop()
                    break
                else:
                    # Asteroid is destroyed
                    break

            else:
                stack.append(x)

        return stack
