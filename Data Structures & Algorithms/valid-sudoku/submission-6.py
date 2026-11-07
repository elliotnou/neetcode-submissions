class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # this is always 1-9/
        # each element in board is a ROW

        rowset = defaultdict(set)
        colset = defaultdict(set)
        boxset = defaultdict(set)

        for r in range(0,9):
            for c in range(0, 9):
                # check if char is "."
                if board[r][c] == ".":
                    continue
                 # check if char is already in rowset
                elif board[r][c] in rowset[r] or board[r][c] in colset[c] or board[r][c] in boxset[(r//3, c//3)]:
                    return False
                else:
                    rowset[r].add(board[r][c])
                    colset[c].add(board[r][c])
                    boxset[(r//3, c//3)].add(board[r][c])
        
        return True
                
                

        