class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        h = {}
        for n in arr:
            h[n] = h.get(n, 0) + 1
            
        return len(set(h.values())) == len(h)