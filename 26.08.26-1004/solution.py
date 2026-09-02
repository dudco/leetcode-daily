class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        fliped = set()
        left = 0
        best = 0
        for right, n in enumerate(nums):
            if n == 0:
                fliped.add(right)

            while len(fliped) > k:
                fliped.discard(left) # 만약 left가 fliped에 존재하면 left는 제거
                left += 1

            best = max(best, right - left + 1)

        return best
