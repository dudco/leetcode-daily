class Solution:
    def removeStars(self, s: str) -> str:
        l = []

        for _, v in enumerate(s):
            if v != "*":
                l.append(v)
            else:
                l.pop()

        return "".join(l)