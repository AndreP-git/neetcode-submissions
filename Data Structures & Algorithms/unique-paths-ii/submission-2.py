class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        # def dp(row: int, col: int):
        #     if row == m or col == n or obstacleGrid[row][col] == 1:
        #         return 0
        #     if row == m-1 and col == n-1:
        #         return 1
        #     if cache[row][col] > 0:
        #         return cache[row][col]

        #     cache[row][col] += dp(row+1, col) + dp(row, col+1)
        #     return cache[row][col]
        
        # m, n = len(obstacleGrid), len(obstacleGrid[0])
        # cache = [[0] * n for _ in range(m)]
        # return dp(0, 0)

        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[m-1][n-1] == 1 or obstacleGrid[0][0] == 1:
            return 0

        prev_row = [0] * (n+1)
        prev_row[n-1] = 1

        for row in range(m-1, -1, -1):
            for col in range(n-1, -1, -1):
                if obstacleGrid[row][col] == 1:
                    prev_row[col] = 0
                elif not (row == m - 1 and col == n - 1):
                    prev_row[col] += prev_row[col+1]
        
        return prev_row[0]
