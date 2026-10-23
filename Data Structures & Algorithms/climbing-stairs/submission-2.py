class Solution:
    def climbStairs(self, n: int) -> int:
        
        def climb(i: int):
            if i <= 2:
                return i
            
            if i in cache:
                return cache[i]
            
            cache[i] = climb(i-1) + climb(i-2)
            return cache[i]
        
        cache = {}
        return climb(n)