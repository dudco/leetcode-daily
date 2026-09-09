## [3871. Count Commas in Range II](https://leetcode.com/problems/count-commas-in-range-ii/description/?envType=daily-question&envId=2026-09-09)

**난이도:** 🟡 Medium

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
- 1 <= n <= 10^15

## 해석 및 풀이 방식
n까지의 숫자들이 사용하는 총 comma의 개수를 세는문제. 10^15 이기에 그냥 무작정 1부터 전달된 n까지 세면 너무 오래걸림

1. 1,000 ~ 999,999 까지 1개 사용 -> 999000개까지는 1개 사용
2. 1,000,000 ~ 999,999,999 까지 2개 사용 1,000,000,000 - 1,000,000 -> 2개 사용
3. 1,000,000,000 ~ 999,999,999,999 까지 3개 사용

10의 3승, 6승, 9승, 12승, 15승마다 쉼표가 하나씩 추가됨.

특정 수가 10의 3승보다 같거나 크면서 10의 6승보다는 작다 -> n - (10^3-1)개

특정 수가 10의 6승보다 같거나 크면서 10의 9승보다는 작다 -> 999,000 + n - (10^6-1) 개

특정 수가 10의 9승보다 같거나 크면서 10의 12승보다는 작다 -> 999,000 + 999,000,000 + n - (10^9-1) 개

특정 수가 10의 12승보다 같거나 크면서 10의 15승보다는 작다 -> 999,000 + 999,000,000 + 999,000,000,000 + n - (10^12-1) 개

특정 수가 10의 15승보다 같다 (클 순 없음) -> 999,000 + 999,000,000 + 999,000,000,000 + 999,000,000,000,000 + 1

만약 특정 수가 10의 6승보다 크다면 10의 3승까지의 숫자는 모두 포함됨 -> 999,000 는 기본으로 사용되는고 1,000,000 부터 n까지 2개씩 증가하는거
---
수학적으로 접근해서 풀긴했는데 코드 줄 수같은거의 최적화가 가능해 보이긴함
### 알고리즘
- 수학

### 시간복잡도: O(1)

### 공간복잡도: O(1)

## 다른사람들의 개쩌는답
https://leetcode.com/problems/count-commas-in-range-ii/solutions/8510746/comma-pattern-range-counting-simple-math-uptf/

가장 수학적으로 접근한 풀이