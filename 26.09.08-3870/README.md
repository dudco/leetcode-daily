## [3870. Count Commas in Range](https://leetcode.com/problems/count-commas-in-range/description/?envType=daily-question&envId=2026-09-08)

**난이도:** 🟢 Easy

### 문제 설명
You are given an integer n.

Return the total number of commas used when writing all integers from [1, n] (inclusive) in standard number formatting.

In standard formatting:

- A comma is inserted after every three digits from the right.
- Numbers with fewer than 4 digits contain no commas.

Example 1:
- Input: n = 1002
- Output: 3
- Explanation:

    The numbers "1,000", "1,001", and "1,002" each contain one comma, giving a total of 3.

Example 2:
- Input: n = 998
- Output: 0
- Explanation:

    All numbers from 1 to 998 have fewer than four digits. Therefore, no commas are used.

Constraints:
- 1 <= n <= 10^5

## 해석 및 풀이 방식
10으로 몇번나눌 수 있는지 확인 후 

### 알고리즘

### 시간복잡도:

### 공간복잡도:

## 다른사람들의 개쩌는답
https://leetcode.com/problems/count-commas-in-range/solutions/8508339/1-by-rovele4569-vp7c/?envType=daily-question&envId=2026-09-08


If n≥1,000, the count of numbers containing a comma is n−999.
If n<1,000, the count is 0.

```
class Solution(object):
    def countCommas(self, n):
        return (n > 999) * (n - 999)
```

이런방법이