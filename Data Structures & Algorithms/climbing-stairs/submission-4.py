class Solution:
    def climbStairs(self, n: int) -> int:
        
        prev = curr = 1

        for i in range(2, n+1):
            tmp = curr
            curr = curr + prev
            prev = tmp
        
        return curr