class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        for idx, n in enumerate(nums):
            if n != 0:
                tmp = nums[l]
                nums[l] = n
                nums[idx]=tmp
                l+=1