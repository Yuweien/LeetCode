# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cntr,w = Counter(s1),len(s1)
        if w > len(s2): return False

        for i in range(len(s2)-w + 1):
            if Counter(s2[i:i+w]) == cntr: return True
        return False
