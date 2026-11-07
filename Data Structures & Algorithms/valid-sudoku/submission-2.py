class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        visited_col = defaultdict(set)
        visited_box = defaultdict(set)
        for r in range(9):
            visited_row = set()
            for c in range(9):
                n = board[r][c]
                if n == ".":
                    continue
                
                
                if n in visited_row or n in visited_col[c] or n in visited_box[(r // 3, c // 3)] or int(n) > 9 or int(n) < 1:
                    return False
                visited_row.add(n)
                visited_col[c].add(n)
                visited_box[(r // 3, c // 3)].add(n)
        return True


            


        
                