class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        l, r = 0, rows - 1
        candidate = - 1

        while l <= r:
            m = l + (r - l) // 2
            if matrix[m][0] <= target:
                candidate = m
                l = m + 1
            else:
                r = m - 1
        if candidate == -1:
            return False

        l, r = 0, cols - 1
        while l <= r:
            m = l + (r - l) // 2
            if matrix[candidate][m] == target:
                return True
            elif matrix[candidate][m] < target:
                l = m + 1
            else:
                r = m - 1
        return False
            

