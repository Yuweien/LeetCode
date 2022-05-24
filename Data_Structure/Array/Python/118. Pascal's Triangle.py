# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows   == 0: return []
        row = [1]
        triangle = [[1]]
        for n in range(1,numRows):
            middle = []
            for i in range(len(row)-1):
                middle.append(row[i]+ row[i+1])
            row = [1] + middle + [1]
            triangle.append(row)
        return triangle

res = Solution()
print(res.generate(numRows = 5))
