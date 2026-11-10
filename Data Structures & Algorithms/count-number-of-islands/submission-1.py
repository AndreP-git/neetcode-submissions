class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(row: int, col: int) -> None:
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                if valid(new_row, new_col) and (new_row, new_col) not in seen:
                    seen.add((new_row, new_col))
                    dfs(new_row, new_col)

        num_islands = 0
        seen = set()
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        valid = lambda r, c: 0 <= r < ROWS and 0 <= c < COLS and grid[r][c] == "1"

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1" and (row, col) not in seen:
                    num_islands += 1
                    seen.add((row, col))
                    dfs(row, col)
        
        return num_islands
        
