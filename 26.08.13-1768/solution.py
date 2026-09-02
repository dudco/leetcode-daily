class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m = min(len(word1), len(word2))

        ret = ""
        for idx in range(m):
            ret += word1[idx] + word2[idx]

        ret += word1[m:] + word2[m:]

        return ret