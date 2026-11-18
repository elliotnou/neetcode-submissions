class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        visitedrows = defaultdict(list)
        visitedcols = defaultdict(list)
        visitedbox = defaultdict(list)
        for r in range(9):

            for c in range(9):
                if board[r][c] == ".":
                    continue
                
                if board[r][c] in visitedrows[r] or board[r][c] in visitedcols[c] or board[r][c] in visitedbox[(r//3, c//3)]:
                    return False
                else:
                    visitedrows[r].append(board[r][c])
                    visitedcols[c].append(board[r][c])
                    visitedbox[(r//3, c//3)].append(board[r][c])
        
        return True
