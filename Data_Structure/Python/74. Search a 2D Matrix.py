# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true

def searchMatrix(matrix, target: int) -> bool:
    if len(matrix) == 0: return False

    r,c = len(matrix),len(matrix[0])
    left, right = 0, r*c-1

    while left <= right:
        pivot_index = (left + right) // 2
        pivot = matrix[pivot_index//c][pivot_index % c]
        if target == pivot: return True
        elif target < pivot:
            right = pivot_index - 1
        elif target > pivot:
            left = pivot_index + 1
    return False

print(searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3))
