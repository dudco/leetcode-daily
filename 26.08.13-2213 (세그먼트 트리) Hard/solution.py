from math import ceil, log2


class Solution:
    def longestRepeating(
        self, s: str, queryCharacters: str, queryIndices: list[int]
    ) -> list[int]:
        h = ceil(log2(len(s)))
        self.tree = [("", "", 0, "", 0, False)] * (1 << (h + 1))
        self.make_segtree(s, 1, 0, len(s) - 1)

        ret = [0] * len(queryIndices)

        for i in range(len(queryIndices)):
            self.insert(queryCharacters[i], queryIndices[i], 1, 0, len(s) - 1)
            ret[i] = self.tree[1][3]

        return ret

    def make_segtree(self, s: str, node: int, start: int, end: int):
        if start == end:
            v = s[start]
            self.tree[node] = self.make_basic_node(v)
            return

        mid = (start + end) // 2
        self.make_segtree(s, node * 2, start, mid)
        self.make_segtree(s, node * 2 + 1, mid + 1, end)

        self.merge_node(node)

    def insert(self, v: str, idx: int, node: int, start: int, end: int):
        if idx < start or idx > end:
            return
        if start == end:
            self.tree[node] = self.make_basic_node(v)
            return

        mid = (start + end) // 2
        if idx <= mid:
            self.insert(v, idx, node * 2, start, mid)
        else:
            self.insert(v, idx, node * 2 + 1, mid + 1, end)
        self.merge_node(node)

    def make_basic_node(self, v: str):
        return (
            v,  # 원본 문자열
            v,  # 시작 문자
            v,  # 끝 문자
            1,  # 가장 많이 맞는 문자열의 개수
            1,  # 접두사 최대길이
            1,  # 접미사 최대길
            True,
        )

    def merge_node(self, node: int):
        left_node = self.tree[node * 2]
        right_node = self.tree[node * 2 + 1]  # c

        merge = left_node[0] + right_node[0]
        start_char = left_node[1]  # 왼쪽 노드의 시작 문자가 새로운 노드의 시작 문자
        end_char = right_node[2]  # 오른쪽 노드의 끝 문자가 새로운 노드의 끝 문자

        # 기본적으로
        max_length = max(
            left_node[3], right_node[3]
        )  # 합쳐진 노드의 최대 길이는 왼쪽노드의 최대길이 혹은 오른쪽 노드의 최대길이
        prefix_length = left_node[
            4
        ]  # 합쳐진 노드의 접두사 최대 길이는 왼쪽 노드의 접두사 최대길이
        suffix_length = right_node[
            5
        ]  # 합쳐진 노드의 접미사 최대 길이는 오른쪽 노드의 접미사 최대길이
        all_eq = left_node[6] and right_node[6]

        if (
            left_node[2] == right_node[1]
        ):  # 만약 왼쪽 노드의 끝 문자와 오른쪽 노드의 시작 문자가 같다면
            merged_char = left_node[2]
            merged_length = (
                left_node[5] + right_node[4]
            )  # 접두사 or 접미사 or 암것도아님 or 다 맞음
            if (
                left_node[6] and merged_char == start_char
            ):  # 만약 왼쪽 노드가 한글자로만 되어있고 시작글자가 합쳐진 글자와 같음 -> 접두사
                prefix_length = merged_length
            if (
                right_node[6] and merged_char == end_char
            ):  # 만약 오른쪽 노드가 한글자로만 되어있고 끝 글자가 합쳐진 글자와 같음 -> 접미사
                suffix_length = merged_length

            max_length = max(
                max_length, merged_length
            )  # 왼쪽 노드의 접미사 최대길이 + 오른쪽 노드의 접미사 최대길이 중 더 긴거
        else:
            all_eq = False

        self.tree[node] = (
            merge,
            start_char,
            end_char,
            max_length,
            prefix_length,
            suffix_length,
            all_eq,
        )
