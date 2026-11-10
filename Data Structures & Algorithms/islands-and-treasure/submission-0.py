class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        INF = 2147483647
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        valid = lambda r, c: 0 <= r < ROWS and 0 <= c < COLS and grid[r][c] == INF
        queue = deque([])

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    queue.append((row, col))
                
        while queue:
            for _ in range(len(queue)):

                row, col = queue.popleft()

                for dx, dy in directions:
                    new_row, new_col = row + dx, col + dy
                    if valid(new_row, new_col):
                        grid[new_row][new_col] = grid[row][col] + 1
                        queue.append((new_row, new_col))
        


