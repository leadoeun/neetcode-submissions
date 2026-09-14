class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            table = {}
            for item in row:
                if item in table and item != ".":
                    return False
                else:
                    table[item] = 1
        for i in range(9):
            table = {}
            for j in range(9):
                item = board[j][i]
                if item in table and item != ".":
                    return False
                else:
                    table[item] = 1
        iterlist = [[0, 0], [0, 3], [0, 6], 
        [3, 0], [3, 3], [3, 6],
        [6, 0], [6, 3], [6, 6]]
        for il in iterlist:
            table = {}
            for i in range(3):
                for j in range (3):
                    item = board[il[0] + i][il[1] + j]
                    if item in table and item != ".":
                        return False
                    else:
                        table[item] = 1

        return True
        