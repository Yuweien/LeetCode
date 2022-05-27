# Input: s = "leetcode"
# Output: 0
def firstUniqChar(s: str) -> int:
    count = {}

    for i in s:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1

    for j in count:
        if count[j] == 1:
            return s.index(j)
    return -1

#n^2 差点超时
def firstUniqChar(s: str) -> int:
    for i in s:
        if s.count(i) == 1:
            return True

    return -1

print(firstUniqChar(s = "aabb"))
