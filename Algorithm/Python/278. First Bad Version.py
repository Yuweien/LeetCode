# Input: n = 5, bad = 4
# Output: 4
# Explanation:
# call isBadVersion(3) -> false
# call isBadVersion(5) -> true
# call isBadVersion(4) -> true
# Then 4 is the first bad version.

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left,right = 1, n  #not start from 0. Because this is the number of elements, not the index of array

        while left < right:
            pivot = (left+right)//2
            if isBadVersion(pivot):
                right = pivot  #keep the right to make sure there's a pointer that points to True
            else:
                left = pivot + 1
        return left #can also be right. But cannot use if left == right at the beginning. Don't know why yet.
