class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack =[]

        for asteroid in asteroids:
            alive = True

            while stack and stack[-1] > 0 and asteroid < 0 and alive:
                if stack[-1] < abs(asteroid):
                    stack.pop()
                elif stack[-1] == abs(asteroid): 
                    stack.pop()
                    alive = False
                else:
                    alive = False
            
            if alive == True:
                stack.append(asteroid)
        return stack