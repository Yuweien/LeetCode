# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n #incase the number exceeds the len of nums

        start = p_idx = count = 0

        while count < n:
            temp = nums[p_idx]
            while True:
                new_idx = (p_idx + k) % n
                nums[new_idx], temp = temp, nums[new_idx]
                p_idx += k
                count += 1
                if start == p_idx % n:
                    break
            start = p_idx = start + 1
