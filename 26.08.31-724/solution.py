class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        t1, t2 = [0], [0]
        l = len(nums)

        for idx in range(l):
            t1.append(t1[-1] + nums[idx])
        for idx in range(l-1, -1, -1):
            t2.append(t2[-1] + nums[idx])

        for i in range(l):
            if t1[i] == t2[l - 1 - i]:
                return i

        return -1