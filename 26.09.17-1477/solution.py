class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        l = s = 0
        best = [float("inf")] * n
        shortest = ans = float("inf")
        for r in range(n):
            s += arr[r]

            while s > target:
                s -= arr[l]
                l+=1

            if s == target:
                length = r - l + 1
                
                # 현재 구간의 왼쪽과 겹치지 않는 이전 구간 확인
                if l > 0 and best[l - 1] != float("inf"):
                    ans = min(ans, best[l - 1] + length)

                shortest = min(shortest, length)

            best[r] = shortest

        return ans if ans != float("inf") else -1