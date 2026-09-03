class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        minOdd = float("inf")
        minEven = float("inf")
        for i in nums1:
            if i % 2 == 0 and minEven > i: minEven = i
            elif i % 2 != 0 and minOdd > i: minOdd = i

        if minOdd == float("inf") or minEven == float("inf"): return True
        return minEven > minOdd
