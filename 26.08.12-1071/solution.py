class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l = min(len(str1), len(str2))
        ret = ""
        for idx in range(l):
            s = str1[0:idx+1]
            if s * int(len(str1)/len(s)) == str1 and s * int(len(str2)/len(s)) == str2:
                ret = s

        return ret