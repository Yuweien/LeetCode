# Input: board =
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

def isValidSudoku(board) -> bool:
    #check rows
    for i in board:
        if len(set(i))+i.count(".") != 10:
            return False
    #check columns
    for j in list(zip(*board)):
        if len(set(j))+j.count(".") != 10:
            return False
    #check 3*3 boxes
    boxes = []
    for r in range(0,7,3):
        for c in range(0,7,3):
            box = [item[c:c+3] for item in board[r:r+3]]
            boxes.append(sum(box,[]))
    for i in boxes:
        if len(set(i))+i.count(".") != 10:
            return False
    else:
        return True


print(isValidSudoku(board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]))
