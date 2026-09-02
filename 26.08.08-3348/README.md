## [3348. Smallest Divisible Digit Product II](https://leetcode.com/problems/smallest-divisible-digit-product-ii/description/?envType=daily-question&envId=2026-08-07)

### 문제 설명
You are given a string num which represents a positive integer, and an integer t.

A number is called zero-free if none of its digits are 0.

Return a string representing the smallest zero-free number greater than or equal to num such that the product of its digits is divisible by t. If no such number exists, return "-1".

 

Example 1:

Input: num = "1234", t = 256

Output: "1488"

Explanation:

The smallest zero-free number that is greater than 1234 and has the product of its digits divisible by 256 is 1488, with the product of its digits equal to 256.

Example 2:

Input: num = "12355", t = 50

Output: "12355"

Explanation:

12355 is already zero-free and has the product of its digits divisible by 50, with the product of its digits equal to 150.

Example 3:

Input: num = "11111", t = 26

Output: "-1"

Explanation:

No number greater than 11111 has the product of its digits divisible by 26.

 

Constraints:

2 <= num.length <= 2 * 10^5

num consists only of digits in the range ['0', '9'].

num does not contain leading zeros.

1 <= t <= 10^14

## 해석 및 풀이 방식
num 을 하나씩 증가시키면서 t로 나눠지는지 확인하는건 매우 비효율적 (num의 길이가 200,000 이라서)

핵심은 각 자릿수의 곱이 t로 나눠지면서 해당 num 에 0이 없으려면 어떻게해야할까 -> 0이 아닌 한 자리 숫자가 만들 수 있는 소인수는 2, 3, 5, 7뿐임
1. 일단 각 자리수는 1~9의 숫자임. 1~9는 2, 3, 5, 7의 곱으로 이뤄짐
2. t에 2, 3, 5, 7이 몇번 곱해져있는지 확인
3. num의 각 자리수의 2, 3, 5, 7 개수 확인 및 0이 있는지 확인
4. 0이 없다면 num 자체가 답일 수 있는지 확인
5. num이 답이 아니고 0이 있으면 0 부분부터 position
6. num이 답이 아니고 0이 없으면 맨 왼쪽부터 position
7. position 을 기준으로 왼쪽 숫자들이 가지고있는 2, 3, 5, 7 개수파악
8. position 에 1을 더하며 해당 숫자가 가지는 2, 3, 5, 7 개수파악
9. 남은 2, 3, 5, 7들을 만족하는 가장 작은 숫자 파악 -> 해당 숫자의 자릿수가 position 기준으로 오른쪽 자리수보다 작다? 그것이 정답
10. 만약 position 에 숫자를 전부대입했는데 답이안나온다? -> 자리수 증가 (position - 1)
11. 만약 position 이 0보다 작아졌다? num 보다 한자리가 더 많은 숫자로 처리

### 알고리즘
`소인수 지수 상태를 이용한 DP로 가능 여부를 판단하면서, 숫자를 가장 작게 만드는 그리디 구성 알고리즘입니다.`
- 소인수분해
- 메모이제이션 DP (min_digits)
- 그리디

### 시간복잡도: O(n + S + \log t)
num을 오른쪽부터 탐색: 각 자리에서 최대 9개 숫자를 확인하므로 O(9n) → O(n)

min_digits: 각 상태에서 숫자 2~9 총 8개를 확인 → O(8S) → O(S)

t 소인수분해: O(\log t)

### 공간복잡도: O(S + n)
@cache가 min_digits의 계산 결과를 저장: O(S)

최종 답 문자열 생성: 최대 O(n) 크기

prefix, total 등 나머지 변수는 상수 크기입니다.

## 다른사람들의 개쩌는답
1. https://leetcode.com/problems/smallest-divisible-digit-product-ii/solutions/8446429/125ms-beats-3276-easy-approach-and-step-w7iaf

2와 3으로 이뤄지는 숫자들을 DP 로 미리 계산한 뒤 5, 7 이 필요한 개수는 그냥 더해서 쿵짝하는듯