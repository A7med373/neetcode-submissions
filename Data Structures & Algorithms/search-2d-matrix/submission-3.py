class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        needed_row = -1

        l, r = 0, rows - 1
        while l <= r:
            m = l + (r - l) // 2
            if matrix[m][0] <= target:
                needed_row = m
                l = m + 1
            else:
                r = m - 1
        if needed_row == - 1:
            return False
        l, r = 0, cols - 1
        while l <= r:
            m = l + (r - l) // 2
            if matrix[needed_row][m] == target:
                return True
            elif matrix[needed_row][m] < target:
                l = m + 1
            else:
                r = m - 1
        return False
