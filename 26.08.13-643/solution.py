class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        res = ret = sum(nums[0:k])/k
        l = 0
        r = k
        for idx in range(len(nums)-k):
            res = res - (nums[l+idx] / k) + (nums[r+idx] / k)
            ret = max(ret, res)

        return ret