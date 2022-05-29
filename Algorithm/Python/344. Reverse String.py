# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s)-1

        while left < right:
            s[left],s[right] = s[right],s[left]
            left += 1
            right -= 1


        #one liner:
        s[:] = s[::-1]
