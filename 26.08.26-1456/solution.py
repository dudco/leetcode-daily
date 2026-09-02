class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        left = 0
        cnt = 0
        best = 0
        for right, char in enumerate(s):
            if char in ('a', 'e', 'i', 'o', 'u'):
                cnt += 1

            if right - left + 1 > k:
                while right - left  + 1 > k:
                    if s[left] in ('a', 'e', 'i', 'o', 'u'):
                        cnt -= 1
                    left += 1

            if right - left + 1 == k:
                best = max(best, cnt)

        return best
                    