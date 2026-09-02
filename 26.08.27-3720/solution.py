class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        lt = len(target)
        source_set = {}

        for _s in sorted(s):
            r = source_set.get(_s, 0)
            source_set[_s] = r + 1
        

        def find(t_i, s):
            if t_i == lt - 1:
                for k, c in source_set.items():
                    if c > 0 and k > target[t_i]: return s + k
                return ""

            for _s, v in source_set.items():
                if _s == target[t_i] and v > 0:
                    source_set[_s] -= 1
                    r = find(t_i+1, s+_s)
                    source_set[_s] += 1
                    if r != "": return r
                elif _s > target[t_i] and v > 0:
                    source_set[_s] -= 1
                    r = s + _s
                    for k, c in source_set.items():
                        r += k * c
                    if r != "": return r

            return ""


        return find(0, "")