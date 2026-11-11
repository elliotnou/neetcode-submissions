"""
- a matrix that is sorted in non-decreasing order
- look for target. if it is in the matrix, return True. False otherwise
- time: O(log(m*n))

- edge cases:
    - target is not inside the matrix
    - matrix is one row, one col

- thinking of using a binary search
- how to handle correct logic for finding midpoint of the rows and cols?
- keep a general number for i where row is i // len(row) and col is i % len(row)

"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        l,r = 0, ROWS * COLS - 1
        while l <= r:
            m = (l+r) // 2
            row = m // COLS
            col = m % COLS
            if matrix[row][col] == target:
                return True
            if matrix[row][col] > target:
                # search right
                r = m-1
            else:
                # search left
                l = m+1

        return False

         