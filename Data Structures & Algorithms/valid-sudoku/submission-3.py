class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # outper loop is for cols, inner loop is for rows
        rowvisited = defaultdict(set)
        colvisited = defaultdict(set)
        boxvisited = defaultdict(set)
        for r, n in enumerate(board):
            for c, m in enumerate(n):
                if m == ".":
                    continue
                elif m in rowvisited[c] or m in colvisited[r] or m in boxvisited[(c // 3, r // 3)]:
                    return False
                else:
                    rowvisited[c].add(m)
                    colvisited[r].add(m)
                    boxvisited[(c//3, r//3)].add(m)
        
        return True
        
            
                
                