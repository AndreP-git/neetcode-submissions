class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        def dp(row: int, col: int):
            if row == m or col == n or obstacleGrid[row][col] == 1:
                return 0
            if row == m-1 and col == n-1:
                return 1
            if cache[row][col] > 0:
                return cache[row][col]

            cache[row][col] += dp(row+1, col) + dp(row, col+1)
            return cache[row][col]
        
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        cache = [[0] * n for _ in range(m)]
        return dp(0, 0)
