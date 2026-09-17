class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7

        # prev_not_end[j]:
        # 지금까지 본 점들로 j개 구간을 만들었고,
        # 마지막 점이 어떤 구간의 끝점도 아닌 경우
        prev_not_end = [0] * (k + 1)

        # prev_end[j]:
        # 지금까지 본 점들로 j개 구간을 만들었고,
        # 마지막 점이 마지막 구간의 끝점인 경우
        prev_end = [0] * (k + 1)

        # 점 0만 본 상태: 구간을 0개 만드는 방법은 1개
        prev_not_end[0] = 1

        # 점 1 ~ n-1을 하나씩 추가
        for _ in range(1, n):
            curr_not_end = [0] * (k + 1)
            curr_end = [0] * (k + 1)

            for segments in range(k + 1):
                # 새 점을 구간 끝점으로 사용하지 않는다.
                curr_not_end[segments] = (
                    prev_not_end[segments] + prev_end[segments]
                ) % MOD

                if segments > 0:
                    curr_end[segments] = (
                        # 기존 마지막 구간을 한 칸 연장
                        prev_end[segments]

                        # 새 구간 [이전 점, 현재 점] 생성
                        # 이전 점이 다른 구간의 끝점이어도 허용됨
                        # → 끝점 공유 케이스를 포함
                        + prev_not_end[segments - 1]
                        + prev_end[segments - 1]
                    ) % MOD

            prev_not_end, prev_end = curr_not_end, curr_end

        return (prev_not_end[k] + prev_end[k]) % MOD