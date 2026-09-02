from collections import Counter

L = "abcdefghijklmnopqrstuvwxyz"

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s); m = n // 2
        cnt = Counter(s)
        odd = [c for c in sorted(cnt) if cnt[c] % 2]
        if len(odd) > n % 2:
            return ""                       # 회문 순열 없음
        mid = odd[0] if odd else ""
        half = Counter({c: v // 2 for c, v in cnt.items() if v // 2})
        make = lambda h: h + mid + h[::-1]

        # 1) 절반 == target[:m] 인 경우 (분기가 가장 늦음 = 최소 후보)
        tmp, ok = Counter(half), True
        for i in range(m):
            if tmp[target[i]] == 0: ok = False; break
            tmp[target[i]] -= 1
        if ok:
            c = make(target[:m])
            if c > target: return c

        # 2) i 에서 target[i] 초과 문자로 분기, i 는 뒤에서부터
        avail = Counter(half); pref = 0
        while pref < m and avail[target[pref]] > 0:
            avail[target[pref]] -= 1; pref += 1
        i = pref
        while i > m - 1:                    # i 를 min(pref, m-1) 로 내리며 복원
            i -= 1; avail[target[i]] += 1
        while i >= 0:
            nxt = next((c for c in L if c > target[i] and avail[c] > 0), None)
            if nxt:
                avail[nxt] -= 1
                h = target[:i] + nxt + "".join(c * avail[c] for c in L)
                return make(h)              # 뒤는 오름차순으로 채우면 최소
            i -= 1
            if i >= 0: avail[target[i]] += 1
        return ""
