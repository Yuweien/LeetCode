# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

from typing import List
def moveZeroes(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    #two pointers
    slow = fast = 0
    while fast < len(nums):
        if nums[slow]==0 and nums[fast]!=0:
            nums[slow],nums[fast] = nums[fast],nums[slow]
        if nums[slow] != 0:
            slow += 1
        fast += 1

    #slowest
    for i in nums:
        if i == 0:
            nums.remove(i)
            nums.append(i)

    #faster
    nums[:] = [n for n in nums if n] + [0] * nums.count(0)
