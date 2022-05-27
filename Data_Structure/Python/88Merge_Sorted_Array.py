from typing import List
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

#where the first m elements denote the elements that should be merged,
# and the last n elements are set to 0 and should be ignored.
# nums2 has a length of n.

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(n):
            nums1[m+i] = nums2[i]
        nums1.sort()
        print(nums1)

res = Solution()
res.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)
res.merge(nums1 = [1], m = 1, nums2 = [], n = 0)
res.merge(nums1 = [0], m = 0, nums2 = [1], n = 1)
