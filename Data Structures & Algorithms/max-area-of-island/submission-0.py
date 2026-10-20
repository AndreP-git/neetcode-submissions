class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def dfs(row: int, col: int) -> int:
            if (not valid(row, col)) \
                or (row, col) in seen \
                or grid[row][col] == 0:
                return 0
            
            curr_area = 0
            seen.add((row, col))
            
            for dx, dy in directions:
                curr_area += dfs(row + dx, col + dy)
            return curr_area + 1

        max_area = 0
        ROWS, COLS = len(grid), len(grid[0])
        seen = set()
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        valid = lambda r, c: 0 <= r < ROWS and 0 <= c < COLS

        for row in range(ROWS):
            for col in range(COLS):
                if (row, col) not in seen and grid[row][col] == 1:
                    curr_area = dfs(row,col)
                    max_area = max(max_area, curr_area)
        
        return max_area