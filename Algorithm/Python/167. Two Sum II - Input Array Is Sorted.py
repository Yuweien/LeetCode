# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low, high = 0, len(numbers)-1

        while low < high:
            sums = numbers[low]+numbers[high]
            if sums < target:
                low += 1
            elif sums > target:
                high -= 1
            else:
                return [low+1, high+1]
