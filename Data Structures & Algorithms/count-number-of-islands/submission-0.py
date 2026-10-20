class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(row: int, col: int):
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy

                if ((new_row, new_col) not in seen) \
                    and valid(new_row, new_col) \
                    and grid[new_row][new_col] == "1":

                    seen.add((new_row, new_col))
                    dfs(new_row, new_col)

        island_count = 0
        ROWS, COLS = len(grid), len(grid[0])
        seen = set()
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        valid = lambda r, c: 0 <= r < ROWS and 0 <= c < COLS

        for row in range(ROWS):
            for col in range(COLS):
                
                if (row, col) not in seen and grid[row][col] == "1":
                    island_count += 1
                    seen.add((row, col))
                    dfs(row,col)
        
        return island_count
