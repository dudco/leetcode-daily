class Solution:
    def countBits(self, n: int) -> list[int]:
        ret = [0] * (n+1)
        for i in range(n+1):
            ret[i] = ret[i >> 1] + (i & 1)
        return ret