class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # column is % n
        # row is // n 

        ROWS = len(matrix)
        COLS = len(matrix[0])
        l, r = 0, ROWS*COLS - 1

        while l <= r:
            m = (l+r)//2
            row = m // COLS
            col = m % COLS
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                r = m-1
            else:
                l = m+1
        
        return False

        
            

            