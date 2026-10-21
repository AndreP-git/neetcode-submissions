class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        seen = set()
        minutes = 0
        fresh_count = 0
        directions = [(0,1),(1,0),(0,-1), (-1,0)]
        valid = lambda r, c: 0 <= r < ROWS and 0 <= c < COLS

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    fresh_count += 1
                elif grid[row][col] == 2:
                    queue.append((row, col))
                    seen.add((row, col))
        
        while fresh_count and queue:
            for _ in range(len(queue)):

                row, col = queue.popleft()
                for dx, dy in directions:
                    new_row, new_col = row + dx, col + dy

                    if valid(new_row, new_col) \
                        and (new_row, new_col) not in seen \
                        and grid[new_row][new_col] == 1:

                        grid[new_row][new_col] = 2
                        fresh_count -= 1
                        seen.add((new_row, new_col))
                        queue.append((new_row, new_col))
            minutes += 1
        
        return minutes if fresh_count == 0 else -1

