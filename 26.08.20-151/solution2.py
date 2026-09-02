class Solution:
    def reverseWords(self, s: str) -> str:
        chars = list(s)
        chars.reverse()

        n = len(chars)
        left = 0
        right = 0
        i = 0

        while i < n:
            while i < n and chars[i] == ' ':
                i += 1

            if i == n:
                break

            while i < n and chars[i] != ' ':
                chars[right] = chars[i]
                right += 1
                i += 1

            # 현재 단어를 다시 뒤집기
            chars[left:right] = chars[left:right][::-1]

            chars[right] = ' '
            right += 1
            left = right

            i += 1  # 공백 하나 건너뛰기

        # 마지막에 추가된 공백 제거
        return ''.join(chars[:right - 1]) if right > 0 else ""