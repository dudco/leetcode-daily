class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        l = nums[0]

        for idx, n in enumerate(nums):
            if n > l: l = n

            s = min(nums[idx:])
            if l - s <= k: return idx
        return -1
