# class Solution:
#     def compress(self, chars: list[str]) -> int:
#         l = r = 0
#         for idx, c in enumerate(chars):
#             if c != chars[r]:
#                 n=""
#                 chars[l] = chars[r]
#                 l += 1
#                 if idx - r > 1: # 해당 요소가 두번이상나오면 (이전 요소는 idx - r개만큼 나옴)
#                     n = str(idx - r)
#                     for i in range(len(n)):
#                         chars[l+i] = n[i]
#                 l += len(n)
#                 r = idx
#         n = ""
#         chars[l] = chars[r]
#         l+=1
#         if idx != r:
#             n = str(idx+1-r)
#             for i in range(len(n)):
#                 chars[l+i] = n[i]

#         chars = chars[:l+len(n)]
        
#         return len(chars)

class Solution:
    def compress(self, chars: list[str]) -> int:
        write = 0
        read = 0

        while read < len(chars):
            start = read
            char = chars[read]

            while read < len(chars) and chars[read] == char:
                read += 1

            chars[write] = char
            write += 1

            count = read - start
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return write