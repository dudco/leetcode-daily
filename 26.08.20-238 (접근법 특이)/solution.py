class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ret = [1]*n

        prefix = 1
        for i in range(n):
            ret[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n - 1, -1, -1):
            ret[i] *= suffix
            suffix *= nums[i]

        return ret