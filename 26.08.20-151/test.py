import unittest

from solution2 import Solution


class SolutionTests(unittest.TestCase):
    def test_case1(self):
        s = Solution()
        self.assertEqual(s.reverseWords("the sky is blue"), "blue is sky the")

    def test_case2(self):
        s = Solution()
        self.assertEqual(s.reverseWords("  hello world  "), "world hello")

    def test_case3(self):
        s = Solution()
        self.assertEqual(s.reverseWords("a good   example"), "example good a")

    def test_case4(self):
        s = Solution()
        self.assertEqual(s.reverseWords("EPY2giL"), "EPY2giL")

    def test_case5(self):
        s = Solution()
        self.assertEqual(
            s.reverseWords(
                " 3c      2zPeO dpIMVv2SG    1AM       o       VnUhxK a5YKNyuG     x9    EQ  ruJO       0Dtb8qG91w 1rT3zH F0m n G wU",
            ),
            "wU G n F0m 1rT3zH 0Dtb8qG91w ruJO EQ x9 a5YKNyuG VnUhxK o 1AM dpIMVv2SG 2zPeO 3c",
        )


if __name__ == "__main__":
    unittest.main()
