class Solution:
    def climbStairs(self, n: int) -> int:
        
        def climb(n: int) -> int:
            if n <= 1:
                return 1
            
            if n in memo:
                return memo[n]
            
            memo[n] = climb(n-1) + climb(n-2)
            return memo[n]

        memo = {}
        return climb(n)