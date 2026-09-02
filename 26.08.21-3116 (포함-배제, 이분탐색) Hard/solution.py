from itertools import combinations
from math import lcm


class Solution:
    def findKthSmallest(self, coins: list[int], k: int) -> int:
        def count(x):
            total = 0
            n = len(coins)

            # 모든 부분집합에 대해 포함-배제
            for size in range(1, n + 1):
                for subset in combinations(coins, size):
                    multiple = 1

                    for coin in subset:
                        multiple = lcm(multiple, coin)

                    # x 이하의 multiple 배수 개수
                    value = x // multiple

                    if size % 2 == 1:   # 1개, 3개, 5개 선택: 더하기
                        total += value
                    else:               # 2개, 4개 선택: 빼기
                        total -= value

            return total

        # 가장 작은 동전만 계속 사용해도 k개의 금액을 만들 수 있으므로
        # 답은 min(coins) * k 이하
        left = 1
        right = min(coins) * k

        # count(x) >= k 가 되는 가장 작은 x 찾기
        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid      # 답이 mid이거나 더 왼쪽
            else:
                left = mid + 1   # mid 이하에는 k개가 부족함

        return left
