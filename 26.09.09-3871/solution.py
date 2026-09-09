class Solution:
    def countCommas(self, n: int) -> int:
        if n >= 10 ** 15:
            ret = ((10**6 - 1) - (10**3 - 1)) * 1
            ret += ((10**9 - 1) - (10**6 - 1)) * 2
            ret += ((10**12 - 1) - (10**9 - 1)) * 3
            ret += ((10**15 - 1) - (10**12 - 1)) * 4
            ret += (n - (10**15 - 1)) * 5
            return ret
        elif n >= 10 ** 12:
            ret = ((10**6 - 1) - (10**3 - 1)) * 1
            ret += ((10**9 - 1) - (10**6 - 1)) * 2
            ret += ((10**12 - 1) - (10**9 - 1)) * 3
            ret += (n - (10**12 - 1)) * 4
            return ret
        elif n >= 10 ** 9:
            ret = ((10**6 - 1) - (10**3 - 1)) * 1
            ret += ((10**9 - 1) - (10**6 - 1)) * 2
            ret += (n - (10**9 - 1)) * 3
            return ret
        elif n >= 10 ** 6:
            ret = (10**6 - 1) - (10**3 - 1) 
            ret += (n - (10**6 - 1)) * 2
            return ret
        elif n >= 10 ** 3:
            ret = n - (10**3 - 1)
            return ret
        return 0