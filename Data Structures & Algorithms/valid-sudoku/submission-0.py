class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        m = n = len(board)

        # check rows
        for i in range(n):
            seen = set()
            for j in range(n):

                curr = board[i][j]

                if curr == ".": continue

                if curr in seen:
                    return False
                
                seen.add(curr)
        
        # check cols
        for j in range(n):
            seen = set()
            for i in range(n):

                curr = board[i][j]

                if curr == ".": continue

                if curr in seen:
                    return False
                
                seen.add(curr)       
        
        # check 3x3 blocks
        seen_one, seen_two, seen_three = set(), set(), set()

        for i in range(n):

            if i == 3 or i == 6:
                seen_one, seen_two, seen_three = set(), set(), set()

            for j in range(n):

                curr = board[i][j]

                if curr == ".": continue

                if j <= 2:
                    if curr in seen_one:
                        return False
                    else:
                        seen_one.add(curr)
                if j > 2 and j <= 5:
                    if curr in seen_two:
                        return False
                    else:
                        seen_two.add(curr)
                if j > 5:
                    if curr in seen_three:
                        return False    
                    else:
                            seen_three.add(curr)               
                    
        return True
