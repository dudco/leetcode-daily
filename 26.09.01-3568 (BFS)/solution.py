from collections import deque


class Solution:
    def minMoves(self, classroom: list[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])

        start = None
        litter_index = {}
        litter_count = 0

        # 시작 위치와 litter 번호 찾기
        for r in range(m):
            for c in range(n):
                if classroom[r][c] == "S":
                    start = (r, c)
                elif classroom[r][c] == "L":
                    litter_index[(r, c)] = litter_count
                    litter_count += 1

        # 수거할 litter가 없으면 이동할 필요 없음
        if litter_count == 0:
            return 0

        all_mask = (1 << litter_count) - 1

        # (행, 열, 수거 상태, 남은 에너지)
        visited = set()
        queue = deque()

        sr, sc = start
        queue.append((sr, sc, 0, energy, 0))
        visited.add((sr, sc, 0, energy))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            r, c, mask, remain, moves = queue.popleft()

            # 모든 litter 수거 완료
            if mask == all_mask:
                return moves

            # 에너지가 0이면 더 이상 이동 불가
            if remain == 0:
                continue

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                # 범위 밖 또는 장애물
                if not (0 <= nr < m and 0 <= nc < n):
                    continue
                if classroom[nr][nc] == "X":
                    continue

                next_remain = remain - 1
                next_mask = mask

                # litter 수거
                if classroom[nr][nc] == "L":
                    idx = litter_index[(nr, nc)]
                    next_mask |= 1 << idx

                # R에 도착하면 에너지 충전
                if classroom[nr][nc] == "R":
                    next_remain = energy

                state = (nr, nc, next_mask, next_remain)

                if state not in visited:
                    visited.add(state)
                    queue.append((nr, nc, next_mask, next_remain, moves + 1))

        return -1
