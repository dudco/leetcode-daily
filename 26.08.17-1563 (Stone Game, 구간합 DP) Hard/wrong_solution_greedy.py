class Solution:
    def stoneGameV(self, stoneValue: list[int]) -> int:
        return self.res(stoneValue, 0)

    def res(self, stoneValue, s):
        if len(stoneValue) == 1:
            return s

        i, ls, rs = self.find_opt_idx(stoneValue)

        l = self.res(stoneValue[:i+1], s + ls)
        r = self.res(stoneValue[i+1:], s + rs)
        return max(l, r)
        
    def find_opt_idx(self, stoneValue):
        s = sum(stoneValue)
        l = 0
        r = s
        i = 0
        min_diff = r - l
        for idx, v in enumerate(stoneValue):
            l += v
            r -= v
            if min_diff >= abs(r - l):
                i = idx
                min_diff = abs(r - l)

        l = sum(stoneValue[:i+1])
        r = sum(stoneValue[i+1:])
        return i, l, r