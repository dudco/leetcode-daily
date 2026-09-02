# 각 숫자가 제공하는 (2, 3, 5, 7)의 지수
from functools import cache


FACTORS = (
    (0, 0, 0, 0),  # 0: 사용하지 않음
    (0, 0, 0, 0),  # 1
    (1, 0, 0, 0),  # 2
    (0, 1, 0, 0),  # 3
    (2, 0, 0, 0),  # 4
    (0, 0, 1, 0),  # 5
    (1, 1, 0, 0),  # 6
    (0, 0, 0, 1),  # 7
    (3, 0, 0, 0),  # 8
    (0, 2, 0, 0),  # 9
)

class Solution:
        # 필요한 소인수 지수를 충족하려면 최소 몇 자리가 필요한지
    @cache
    def min_digits(self, a: int, b: int, c: int, d: int) -> int:
        if a == b == c == d == 0:
            return 0

        state = (a, b, c, d)
        answer = float("inf")

        for vec in FACTORS[2:]:  # 2 ~ 9만 사용
            nxt = tuple(max(0, state[i] - vec[i]) for i in range(4))

            # 현재 필요한 인수를 하나도 줄이지 못하는 숫자는 제외
            if nxt != state:
                answer = min(answer, 1 + self.min_digits(*nxt))

        return answer

    def make_smallest_suffix(self, need, slots: int) -> str:
        """
        slots 자리 안에서 need를 만족하는 가장 작은 suffix.
        남는 자리는 앞쪽을 1로 채운다.
        """
        factor_digit_count = self.min_digits(*need)
        result = ["1"] * (slots - factor_digit_count)

        while factor_digit_count > 0:
            # 작은 숫자부터 넣을 수 있는지 확인
            for digit in range(2, 10):
                nxt = tuple(
                    max(0, need[i] - FACTORS[digit][i])
                    for i in range(4)
                )

                if 1 + self.min_digits(*nxt) == factor_digit_count:
                    result.append(str(digit))
                    need = nxt
                    factor_digit_count -= 1
                    break

        return "".join(result)
    
    def smallestNumber(self, num: str, t: int) -> str:
        # t에 2, 3, 5, 7이 몇개씩 곱해져있는지 파악

        required = []
        rest = t

        for prime in (2, 3, 5, 7):
            count = 0
            while rest % prime == 0:
                rest //= prime
                count += 1
            required.append(count)

        required = tuple(required)
        n = len(num)

        # 만약 2, 3, 5, 7 외의 소인수가 있다? -> 해당하는 숫자를 만족하는 zero_free 는 존재할 수 없음
        if rest != 1:
            return "-1"

        # num 에 2, 3, 5, 7 이 몇개씩 곱해져있는지 파악
        total = [0, 0, 0, 0]
        has_zero = False

        for ch in num:
            if ch == "0":
                has_zero = True
                continue

            vec = FACTORS[ord(ch) - ord("0")]
            for i in range(4):
                total[i] += vec[i]

        # num 이 답인지 확인
        if not has_zero and all(total[i] >= required[i] for i in range(4)):
            return num

        # 바꿔야하는 자릿수 앞의 숫자들이 2,3,5,7을 몇개 가지고있는지 확인
        first_zero = num.find("0")
        if first_zero == -1:
            pos = n - 1
            prefix = total[:]
            vec = FACTORS[int(num[pos])]
            for i in range(4):
                prefix[i] -= vec[i]
        else:
            pos = first_zero
            prefix = [0,0,0,0]
            for ch in num[:pos]:
                vec = FACTORS[ord(ch) - ord("0")]
                for i in range(4):
                    prefix[i] += vec[i]

        while pos >= 0:
            suffix_slots = n - pos - 1

            for digit in range(int(num[pos]) + 1, 10):
                # 추가적으로 필요한 2,3,5,7 확인
                vec = FACTORS[digit]
                need = tuple(max(0, required[i]-prefix[i]-vec[i]) for i in range(4))

                if self.min_digits(*need) <= suffix_slots:
                    return (
                        num[:pos]
                        + str(digit)
                        + self.make_smallest_suffix(need, suffix_slots)
                    )

            pos -= 1

            if pos >= 0:
                vec = FACTORS[int(num[pos])]
                for i in range(4):
                    prefix[i] -= vec[i]


        length = max(n + 1, self.min_digits(*required))
        return self.make_smallest_suffix(required, length)