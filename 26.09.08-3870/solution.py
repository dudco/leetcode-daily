class Solution:
    def countCommas(self, n: int) -> int:
        if n < 1000:
            return 0
        div = int(n / 1000)
        ret = n % 1000
        if ret > 1000:
            ret = n  % 1000
        while div != 1:
            ret += 1000
            div -= 1
        return ret + 1
    