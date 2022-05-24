# Input: mat = [[1,2],[3,4]], r = 1, c = 4
# Output: [[1,2,3,4]]

# Input: mat = [[1,2],[3,4]], r = 2, c = 4
# Output: [[1,2],[3,4]]

from typing import List

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        outMatrix = []
        items = sum(mat, [])
        if len(items) == r*c:
            for i in range(0, len(items), c):
                outMatrix.append(items[i:i+c])
        else:
            return mat
        return outMatrix

res = Solution()
print(res.matrixReshape(mat = [[1,2],[3,4]], r = 1, c = 4))
