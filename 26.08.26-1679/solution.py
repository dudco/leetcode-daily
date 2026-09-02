class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        nums.sort()

        left = 0
        right = len(nums) - 1

        ret = 0
        while left < right:
            if nums[left] + nums[right] < k:
                left += 1
            elif nums[left] + nums[right] > k:
                right -= 1
            else:
                ret += 1
                right -= 1
                left += 1

        return ret