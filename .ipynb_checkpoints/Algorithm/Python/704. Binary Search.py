# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4

from typing import List

def search(nums: List[int], target: int) -> int:
    if nums[0] > target or nums[-1] < target: return -1

    left,right = 0, len(nums)

    while left <= right:
        pivot = (left+right) // 2
        if target == nums[pivot]:
            return pivot
        elif target < nums[pivot]:
            right = pivot - 1
        else:
            left = pivot + 1
    return -1

print(search(nums = [-1,0,3,5,9,12], target = 9))
