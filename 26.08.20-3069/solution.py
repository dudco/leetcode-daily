class Solution:
    def resultArray(self, nums: list[int]) -> list[int]:
        arr1 = [nums[0]]
        arr2 = [nums[1]]

        for idx in range(2, len(nums)):
            if arr1[-1] > arr2[-1]:
                arr1.append(nums[idx])
            else:
                arr2.append(nums[idx])

        return [*arr1, *arr2]