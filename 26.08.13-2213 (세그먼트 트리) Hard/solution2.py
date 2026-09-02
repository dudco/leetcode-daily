from sortedcontainers import SortedList


class Solution:
    def longestRepeating(self, s: str, chars: str, indices: list[int]) -> list[int]:
        s = list(s)  # Python 문자열은 수정할 수 없으므로 리스트로 변환
        n = len(s)

        # 경계 위치와, 현재 존재하는 구간 길이들
        boundaries = SortedList([0, n])
        lengths = SortedList()
        count = [0] * (n + 1)

        def add_len(length: int) -> None:
            count[length] += 1
            if count[length] == 1:
                lengths.add(length)

        def remove_len(length: int) -> None:
            count[length] -= 1
            if count[length] == 0:
                lengths.remove(length)

        # 초기 경계 생성
        # boundary i: s[i - 1] != s[i], 즉 새 반복 구간이 i에서 시작
        prev = 0
        for i in range(1, n):
            if s[i - 1] != s[i]:
                boundaries.add(i)
                add_len(i - prev)
                prev = i

        add_len(n - prev)

        def update_boundary(pos: int, add_boundary: bool) -> None:
            if add_boundary:
                # [prev, next] 구간을 [prev, pos], [pos, next]로 분리
                idx = boundaries.bisect_left(pos)
                next_pos = boundaries[idx]
                prev_pos = boundaries[idx - 1]

                remove_len(next_pos - prev_pos)
                add_len(pos - prev_pos)
                add_len(next_pos - pos)

                boundaries.add(pos)

            else:
                # [prev, pos], [pos, next]를 [prev, next]로 병합
                idx = boundaries.bisect_left(pos)
                prev_pos = boundaries[idx - 1]
                next_pos = boundaries[idx + 1]

                remove_len(pos - prev_pos)
                remove_len(next_pos - pos)
                add_len(next_pos - prev_pos)

                boundaries.remove(pos)

        result = []

        for q, idx in enumerate(indices):
            c = chars[q]

            # idx 위치의 문자를 바꾸면 경계 idx와 idx + 1만 영향받음
            if idx > 0: # 현재 위치 왼쪽과 확인
                old_boundary = s[idx - 1] != s[idx] # 원래 바운더리였냐?
                new_boundary = s[idx - 1] != c # 새롭게 추가될 바운더리인가?

                if old_boundary != new_boundary: # 두개가 다르면 제거하거나 추가하거나 해야함 , 만약 같으면 (원래 바운더리도 아니고 새롭게 추가된 바운더리도아님 -> 바운더리 추가처리안됨 / 원래 바운도리이고 새롭게 추가될 바운더리 -> 이미 추가되어있잖아)
                    update_boundary(idx, new_boundary)

            if idx + 1 < n: # 현재 위치 오른쪽과 확인
                old_boundary = s[idx] != s[idx + 1]
                new_boundary = c != s[idx + 1]

                if old_boundary != new_boundary:
                    update_boundary(idx + 1, new_boundary)

            s[idx] = c
            result.append(lengths[-1])  # 가장 긴 반복 구간 길이

        return result
