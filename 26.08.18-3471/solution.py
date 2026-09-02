class Solution:
    def largestInteger(self, nums: list[int], k: int) -> int:
        h = {}
        chk = [False] * 51
        for idx in range(k):
            if chk[nums[idx]]:
                continue
            h[nums[idx]] = h.get(nums[idx], 0) + 1
            chk[nums[idx]] = True


        for l in range(1, len(nums)-k+1):
            chk = [False] * 51
            for idx in range(k):
                if chk[nums[l+idx]]:
                    continue
                h[nums[l+idx]] = h.get(nums[l+idx], 0) + 1
                chk[nums[l+idx]] = True

        ret = -1
        for _k, _v in h.items():
            if _v == 1 and ret < _k:
                ret = _k

        return ret