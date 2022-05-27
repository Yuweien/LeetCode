# Input: ransomNote = "a", magazine = "b"
# Output: false

# For each char in ransomNote:
#     Find that letter in magazine.
#     If it is in magazine:
#         Remove it from magazine.
#     Else:
#         Return False
# Return True

#Time Complexity : O(m \cdot n)O(m⋅n).

# Something you might notice when you run code for this problem here on Leetcode is that Approach 1 passes, and is the fastest. This is because all the testcases are very small. For huge test cases though, the other approaches would beat it, and Approach 1 would be far too slow.

# In an interview, it's unlikely that Approach 1 would be sufficient to get you the job. Interviewers will expect to see an optimized approach such as Approach 2 or 3.

# "aab"
# "baa"
# True
import collections

def canConstruct(ransomNote: str, magazine: str) -> bool:
    return not collections.Counter(ransomNote) - collections.Counter(magazine)

print(canConstruct(ransomNote = "a", magazine = "b"))


# **Explanation** Taking the count of ransomNote and subtracting it with the count of magazine. IF it gets completely subtracted -> Ransomnote is contained in magazine.
#    i.e  Counter('aa') - Counter('aab') = Counter()  ; Returning a not with it will return the desired value.
# also can do: return (Counter(ransomeNote) - Counter(magazine)) == {}
