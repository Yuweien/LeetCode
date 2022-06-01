# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

#Given a string s, find the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        len_s = len(s)
        if len_s == 0: return 0
        if len_s == 1: return 1

        left,right = 0, 1
        longest = 0
        while right < len_s:
            if s[right] in s[left:right]:
                left = left + s[left:right].index(s[right]) + 1
                print(left)
            right += 1

            if right - left > longest:
                longest = right - left

        return longest




        #simpler method:
        #if char not in temp, temp.find(char) = -1, keep the current temp
        #if char in temp, temp.find(char) = the index of the repeated char, keep chars after the repeated one
        len_s = len(s)
        if len_s < 2: return len_s
        temp = ""
        longest = 0
        for char in s:
            temp=temp[temp.find(char)+1:]
            temp+=char
            longest = max(len(temp), longest)
        return longest
