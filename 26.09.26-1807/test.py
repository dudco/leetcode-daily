import unittest

import solution


class SolutionTests(unittest.TestCase):
    def test_case1(self):
        s = solution.Solution()
        self.assertEqual(s.evaluate("(name)is(age)yearsold", [["name", "bob"], ["age", "two"]]), "bobistwoyearsold")

    def test_case2(self):
        s = solution.Solution()
        self.assertEqual(s.evaluate("hi(name)", [["a", "b"]]), "hi?")

    def test_case3(self):
        s = solution.Solution()
        self.assertEqual(s.evaluate("(a)(a)(a)aaa", [["a", "yes"]]), "yesyesyesaaa")

if __name__ == '__main__':
    unittest.main()
