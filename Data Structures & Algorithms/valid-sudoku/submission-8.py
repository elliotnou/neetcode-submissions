class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowvisited = defaultdict(set)
        colvisited = defaultdict(set)
        boxvisited = defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in colvisited[c] or board[r][c] in rowvisited[r] or board[r][c] in boxvisited[(r//3, c//3)]:
                    return False
                else:
                    colvisited[c].add(board[r][c])
                    rowvisited[r].add(board[r][c])
                    boxvisited[(r//3, c//3)].add(board[r][c])
        
        return True
            