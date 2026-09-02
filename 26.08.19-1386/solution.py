class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: list[list[int]]) -> int:
        h = {}

        g1 = 15 << 2 # 1111 << 2
        g2 = 15 << 4 # 1111 << 4
        g3 = 15 << 6 # 1111 << 6

        for seat in reservedSeats:
            state = h.get(seat[0], 0)
            state += 2 ** seat[1]
            h[seat[0]] += state

        ans = (n - len(h))*2
        for v in h.values():
            if v & g1 == 0 and v & g3 == 0:
                ans += 2
            elif v & g1 == 0 or v & g2 == 0 or v & g3 == 0:
                ans += 1

        return ans