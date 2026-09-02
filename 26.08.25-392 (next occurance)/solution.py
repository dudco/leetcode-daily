# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
#         def find(l, r):
#             if l == len(s): return True
#             while True:
#                 if r >= len(t): return False

#                 if s[l] == t[r]:
#                     return find(l+1, r+1)
#                 r+=1
#         return find(0, 0)

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n = len(t)
        next_occurance = [[-1] * 26 for _ in range(n + 1)]
        for i in range(len(t)-1, -1, -1):
            next_occurance[i] = next_occurance[i+1].copy()
            next_occurance[i][ord(t[i])-ord("a")] = i

        pos = 0
        for c in s:
            found = next_occurance[pos][ord(c)-ord("a")]
            if found == -1:
                return False
            pos = found + 1
        return True