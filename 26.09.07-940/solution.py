class Solution:
    def distinctSubseqII(self, s: str) -> int:
        # dp[i] = text[:i]로 만들 수 있는 서로 다른 부분 수열 개수
        # 빈 문자열을 포함하므로 dp[0] = 1
        dp = [1]

        # 각 문자가 마지막으로 등장했던 위치 (1부터 시작하는 인덱스)
        last_index = {}

        for i, char in enumerate(s, start=1):
            # 기존 부분 수열 각각에 char를 붙이거나, 붙이지 않는 경우
            count = (2 * dp[i - 1]) % (10**9 + 7)

            # 같은 문자가 이전에 있었다면 중복 생성된 부분 수열 제거
            if char in last_index:
                previous_position = last_index[char]
                count = (count - dp[previous_position - 1]) % (10**9 + 7)

            dp.append(count)
            last_index[char] = i

        # 빈 문자열 제외
        return (dp[-1] - 1) % (10**9 + 7)

            
