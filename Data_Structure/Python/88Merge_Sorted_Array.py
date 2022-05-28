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

        #another method:two pointers, add to numsq in descending order
        n1_idx, n2_idx = m-1, n-1  #descending order
        counter = m+n-1

        while counter >= 0:
            if n1_idx < 0:
                nums1[counter] = nums2[n2_idx] #if n1 is done, only need to add n2 numbers
                n2_idx -= 1
            elif n2_idx < 0:
                nums1[counter] = nums1[n1_idx] #if n2 is done
                n1_idx -= 1
            elif nums1[n1_idx] <= nums2[n2_idx]:
                nums1[counter] = nums2[n2_idx]
                n2_idx -= 1
            else:
                nums1[counter] = nums1[n1_idx]
                n1_idx -= 1
            counter -= 1

res = Solution()
res.merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)
res.merge(nums1 = [1], m = 1, nums2 = [], n = 0)
res.merge(nums1 = [0], m = 0, nums2 = [1], n = 1)
