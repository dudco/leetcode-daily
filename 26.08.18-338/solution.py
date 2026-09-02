# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

I = 6

def guess(num: int) -> int:
    if num > I:
        return -1
    elif num < I:
        return 1
    else:
        return 0

class Solution:
    def guessNumber(self, n: int) -> int:
        l = 0
        r = n
        g = -1
        while True:
            ret = (l + r) // 2
            g = guess(ret)
            if g > 0:
                l = ret + 1
            elif g < 0:
                r = ret - 1
            else:
                return ret