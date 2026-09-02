class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        lp = 0
        cnt = {}
        ret = 0
        for rp in range(len(s)):
            cnt[s[rp]] = cnt.get(s[rp], 0) + 1
            while(cnt.get(s[rp], 0) > 2):
                cnt[s[lp]] -= 1
                lp += 1

            ret = max(ret, rp-lp+1)

        return ret