# Input: s = "anagram", t = "nagaram"
# Output: true

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False #could be faster
        return sorted(s) == sorted(t)

res = Solution()
print(res.isAnagram(s = "anagram", t = "nagaram"))
