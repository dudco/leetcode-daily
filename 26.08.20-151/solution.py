class Solution:
    def reverseWords(self, s: str) -> str:
        lq = []
        rq = []
        l = len(s)

        ls = le = 0
        rs = re = l

        while True:
            while s[ls] == ' ': ls += 1
            le = ls + 1
            while le < l and s[le] != ' ': le += 1

            while s[re-1] == ' ': re -= 1
            rs = re
            while rs-1 >= 0 and s[rs-1] != ' ': rs -= 1

            if ls == rs and le == re:
                lq.append(s[ls:le])
                break
            elif ls > rs and le > re:
                break
                        

            lq.append(s[ls:le])
            rq.append(s[rs:re])

            ls = le + 1
            re = rs - 1

        ret = " ".join(rq)

        if ret != "":
            ret += " "

        ret += " ".join(lq[::-1])

        return ret