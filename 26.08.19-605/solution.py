class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        for idx, f in enumerate(flowerbed):
            if f == 0: # 없으면 심기
                if idx < len(flowerbed) - 1 and flowerbed[idx + 1] != 0:
                    continue
                if idx - 1 >= 0:
                    flowerbed[idx - 1] = 2
                if idx + 1 < len(flowerbed):
                    flowerbed[idx + 1] = 2
                flowerbed[idx] = 1
                n -= 1
                if n == 0:
                    return True
            if f == 1: # 해당 구역에 심어져있으면 이전, 다음을 2로 변경
                if idx - 1 >= 0:
                    flowerbed[idx - 1] = 2
                if idx + 1 < len(flowerbed):
                    flowerbed[idx + 1] = 2

        return n <= 0
    