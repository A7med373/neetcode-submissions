class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        l, r = 0, rows - 1
        while l < r:
            m = l + (r - l) // 2
            if matrix[m][0] < target:
                l = m + 1
            elif matrix[m][0] > target:
                r = m 
            elif matrix[m][0] == target:
                return True
            
        
        needed_row = l - 1
        l, r = 0, cols - 1
        while l < r:
            m = l + (r - l) // 2
            if matrix[needed_row][m] > target:
                r = m - 1
            elif matrix[needed_row][m] < target:
                l = m + 1
            elif matrix[needed_row][m] == target:
                return True
            else:
                return False
        return False
            

