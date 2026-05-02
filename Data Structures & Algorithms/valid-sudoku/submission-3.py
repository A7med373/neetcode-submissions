class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for row in range(n):
            for col in range(n):
                if board[row][col] == '.':
                    continue
                
                num = board[row][col]
                if (num in rows[row] or num in cols[col] or num in squares[(row // 3, col // 3)]):
                    return False
                rows[row].add(num)
                cols[col].add(num)
                squares[(row // 3, col // 3)].add(num)
        return True
