class Solution:
    def reverseVowels(self, s: str) -> str:
        l = 0
        r = len(s) - 1
        ret = list(s)
        while l < r:
            if s[l] not in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
                l += 1

            if s[r] not in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
                r -= 1

            if s[l] in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U') and s[r] in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
                ret[l], ret[r] = ret[r], ret[l]
                l += 1
                r -= 1

        return "".join(ret)