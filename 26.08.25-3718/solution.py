class Solution:
    def missingMultiple(self, nums: list[int], k: int) -> int:
        set_of_nums = set(nums)
        i = 1
        while k <= 100:
            if k * i not in set_of_nums:
                return k * i
            i+=1