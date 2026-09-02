class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        m = max(*candies)

        ret = [False] * len(candies)
        for idx, c in enumerate(candies):
            ret[idx] = c + extraCandies >= m

        return ret