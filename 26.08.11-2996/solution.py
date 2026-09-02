class Solution:
    def missingInteger(self, nums: list[int]) -> int:
        idx = 0

        for idx in range(1, len(nums)):
            if nums[idx - 1] + 1 != nums[idx]:
                idx -= 1
                break
                

        data = sum(nums[0:idx+1])


        while(data in nums):
            data += 1

        return data