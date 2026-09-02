class Solution:
    def maxSubarrayLength(self, nums: list[int], k: int) -> int:
        l = 0
        r = 0
        cnts = {}
        ret = 0
        while r < len(nums):
            cnt = cnts.get(nums[r], 0)
            if cnt < k:
                cnts[nums[r]] = cnt + 1
                r += 1
            else:
                cnts[nums[l]] -=1
                l += 1

            ret = max(ret, r - l)

        return ret