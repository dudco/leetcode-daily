from itertools import combinations


class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        ret = []
        for n in range(len(nums)+1):
            ret.extend(combinations(nums, n))

        return ret