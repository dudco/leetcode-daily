class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        sorted_num = sorted(nums)
        l = 0
        r = len(sorted_num) - 1

        while(sorted_num[l] + sorted_num[r] != target):
            if sorted_num[l] + sorted_num[r] > target:
                r -= 1
            else:
                l += 1

        l = nums.index(sorted_num[l])
        for idx in range(len(nums) - 1, -1, -1):
            if nums[idx] == sorted_num[r]:
                r = idx
                break

        return [min(l, r), max(l, r)]
        