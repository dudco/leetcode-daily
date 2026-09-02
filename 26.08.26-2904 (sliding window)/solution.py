class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        left = cnt = 0
        best = None

        for right, char in enumerate(s):
            if char == "1": cnt+=1
            while cnt > k:
                if s[left]=="1":
                    cnt-=1
                left+=1

            while cnt == k and s[left] == "0":
                left+=1

            if cnt == k:
                candidate = s[left:right+1]
                if (
                    best is None
                    or len(candidate) < len(best)
                    or (len(candidate) == len(best) and candidate < best)
                ):
                    best = candidate

        return best or ""