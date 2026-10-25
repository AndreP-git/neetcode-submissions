class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        # def dp(row: int, col: int):
        #     if row == m or col == n:
        #         return 0
        #     if row == m-1 and col == n-1:
        #         return 1
        #     if cache[row][col] > 0:
        #         return cache[row][col]

        #     cache[row][col] = dp(row+1, col) + dp(row, col+1)
        #     return cache[row][col]
        
        # cache = [[0] * n for _ in range(m)]
        # return dp(0, 0)

        cache = [[0] * (n+1) for _ in range(m+1)]
        cache[m-1][n-1] = 1

        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                cache[r][c] += cache[r+1][c] + cache[r][c+1]
        
        return cache[0][0]