class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        ns1 = set(nums1)
        ns2 = set(nums2)
        return [list(ns1 - ns2), list(ns2 - ns1)]