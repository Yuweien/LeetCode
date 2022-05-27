# Input: nums = [1,3,5,6], target = 5
# Output: 2

from typing import List

from numpy import right_shift

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1

        while left <= right:
            pivot = (left+right) // 2
            if target == nums[pivot]:
                return pivot
            elif target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1
        return left #because the last +1 move left to the next position
