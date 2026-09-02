class Solution:
    def maxArea(self, height: list[int]) -> int:
        r = len(height) - 1
        l = 0
        ret = (r - l) * min(height[l], height[r]) # 전체라고 가정

        while l < r:
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
            m = min(height[l], height[r])
            ret = max(ret, (r - l) * m)

        return ret