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
                
                box = 0
                if r // 3 == 0 and c // 3 == 0:
                    box = 0
                elif r // 3 == 1 and c // 3 == 0:
                    box = 1
                elif r // 3 == 2 and c // 3 == 0:
                    box = 2
                elif r // 3 == 0 and c // 3 == 1:
                    box = 3
                elif r // 3 == 1 and c // 3 == 1:
                    box = 4
                elif r // 3 == 2 and c // 3 == 1:
                    box = 5
                elif r // 3 == 0 and c // 3 == 2:
                    box = 6
                elif r // 3 == 1 and c // 3 == 2:
                    box = 7
                elif r // 3 == 2 and c // 3 == 2:
                    box = 8
                
                if n in visited_row or n in visited_col[c] or n in visited_box[box] or int(n) > 9 or int(n) < 1:
                    return False
                visited_row.add(n)
                visited_col[c].add(n)
                visited_box[box].add(n)
        return True


            


        
                