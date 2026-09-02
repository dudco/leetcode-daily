class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        tuples = []
        t = [None, None]
        for idx, n in enumerate(nums):
            if t[0] is None and n == 1:
                # 앞에 1이 나온적이 없는 상태(t[0] is None)에서 1이 등장
                t[0] = idx
            elif t[0] is not None and t[1] is None and n == 0:
                # 앞에 1이 나온적이 있고 (t[1] is not None), 이후 0이 나온경우
                t[1] = idx
                tuples.append(t)
                t = [None, None]

        if t[0] is not None and t[1] is None:
            # t[0] 은 채워졌는데 t[1] 은 안채워졌다는건 1로 끝났다는것
            # 반대로 t[0]이 안채줘있다면 0으로 끝났다는것
            t[1] = idx + 1
            tuples.append(t)

        ret = 0
        for idx, t in enumerate(tuples):
            ret = max(ret, t[1] - t[0])

            if idx < len(tuples) -1 and tuples[idx+1][0] - t[1] == 1:
                ret = max(ret, tuples[idx+1][1] - t[0] - 1)
        l = len(tuples)

        # 만약 1을 이루는 부분 수열이 하나뿐이고
        if l == 1 and ret == len(nums): return ret - 1 # 그 때 해당 부분수열의 길이가 nums의 길이와 같다 -> nums 전체가 1로 이루어짐 -> 무조건 하나는 지워야하니 ret - 1

        return ret
                    