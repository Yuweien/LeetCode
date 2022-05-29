# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"

class Solution:
    def reverseWords(self, s: str) -> str:
        res = " ".join(word[::-1] for word in s.split())
        return res
