class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        def dfs(row: int, col: int):
            directions = [(0,1),(1,0),(0,-1),(-1,0)]
            image[row][col] = color
            
            for dx, dy in directions:

                new_row, new_col = row + dx, col + dy
                if valid(new_row, new_col) and image[new_row][new_col] == orig_color:
                    dfs(row + dx, col + dy)

        if image[sr][sc] == color:
            return image
            
        ROWS, COLS = len(image), len(image[0])
        valid = lambda r, c: 0 <= r < ROWS and 0 <= c < COLS
        orig_color = image[sr][sc]

        dfs(sr, sc)
        return image