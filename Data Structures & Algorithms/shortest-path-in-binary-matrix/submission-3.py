class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        
        # 0 1 0
        # 0 0 0
        # 1 0 0

        if grid[0][0] == 1: return -1

        n = len(grid)
        queue = deque([(0,0)])
        seen = {(0,0)}
        length = 1
        directions = [(1,0),(0,1),(-1,0),(0,-1),(1,-1),(-1,1),(1,1),(-1,-1)]
        valid = lambda r, c: 0 <= r < n and 0 <= c < n

        while queue:
            size = len(queue)

            for _ in range(size):
                row, col = queue.popleft()

                if row == n-1 and col == n-1:
                    return length

                for dx, dy in directions:
                    new_row, new_col = row + dx, col + dy

                    if (new_row, new_col) not in seen \
                        and valid(new_row, new_col) \
                        and grid[new_row][new_col] == 0:
                        seen.add((new_row, new_col))
                        queue.append((new_row, new_col))
            length += 1
        
        return -1
                
