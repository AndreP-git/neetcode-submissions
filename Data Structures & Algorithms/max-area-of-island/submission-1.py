class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        # [0,1,1,0,1]
        # [1,0,1,0,1]
        # [0,1,1,0,1]
        # [0,1,0,0,1]

        def dfs(row: int, col: int) -> int:
            if not valid(row, col):
                return 0
            
            curr_area = 1
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                if valid(new_row, new_col) and (new_row, new_col) not in seen:
                    seen.add((new_row, new_col))
                    curr_area += dfs(new_row, new_col)
            return curr_area

        max_area = 0
        seen = set()
        ROWS, COLS = len(grid), len(grid[0])
        valid = lambda r, c: 0 <= r < ROWS and 0 <= c < COLS and grid[r][c] == 1
        directions = [(0,1),(1,0),(-1,0),(0,-1)]

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1 and (row, col) not in seen:
                    seen.add((row, col))
                    area = dfs(row, col)
                    max_area = max(max_area, area)
        
        return max_area
                        