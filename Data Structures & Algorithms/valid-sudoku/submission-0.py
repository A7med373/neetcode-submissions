class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        dictionary = {}
        for i in range(n):
            unique = set()
            for num in board[i]:
                if num == '.':
                    continue
                if num in unique:
                    return False
                unique.add(num)
            unique2 = set()
            for j in range(n):
                if board[i][j] == '.':
                    continue
                if board[i][j] in unique2:
                    return False
                unique2.add(board[i][j])
                key = (i // 3, j // 3)
                if key not in dictionary:
                    dictionary[key] = set()
                if board[i][j] in dictionary[key]:
                    return False
                dictionary[key].add(board[i][j])
        return True