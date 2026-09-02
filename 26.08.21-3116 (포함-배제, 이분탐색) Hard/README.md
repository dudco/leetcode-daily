## [3116. Kth Smallest Amount With Single Denomination Combination](https://leetcode.com/problems/kth-smallest-amount-with-single-denomination-combination/description/?envType=daily-question&envId=2026-08-21)

### 문제 설명
You are given an integer array coins representing coins of different denominations and an integer k.

You have an infinite number of coins of each denomination. However, you are not allowed to combine coins of different denominations.

Return the kth smallest amount that can be made using these coins.

Example 1:
- Input: coins = [3,6,9], k = 3
- Output: 9
- Explanation: The given coins can make the following amounts:

    Coin 3 produces multiples of 3: 3, 6, 9, 12, 15, etc.
    
    Coin 6 produces multiples of 6: 6, 12, 18, 24, etc.
    
    Coin 9 produces multiples of 9: 9, 18, 27, 36, etc.

    All of the coins combined produce: 3, 6, 9, 12, 15, etc.

Example 2:
- Input: coins = [5,2], k = 7
- Output: 12
- Explanation: The given coins can make the following amounts:
    
    Coin 5 produces multiples of 5: 5, 10, 15, 20, etc.
    
    Coin 2 produces multiples of 2: 2, 4, 6, 8, 10, 12, etc.
    
    All of the coins combined produce: 2, 4, 5, 6, 8, 10, 12, 14, 15, etc.

Constraints:
- 1 <= coins.length <= 15
- 1 <= coins[i] <= 25
- 1 <= k <= 2 * 10^9
- coins contains pairwise distinct integers.

## 해석 및 풀이 방식
동전들을 조합해서 만들 수 있는 숫자들 중 k번째 숫자를 찾는 문제

동전들의 조합은 쉽게 만들지만 k가 2 * 10^9로 엄청나게 큼

단순 앞에서부터 k번째를 세면 엄청 오래걸림.

Binary search the answer x.

Use the inclusion-exclusion principle to count the number of distinct amounts that can be made up to x.

--- 너무 어렵 ;;

coins 를 조합해서 특정 숫자 m까지 몇개의 숫자가 존재하는지 확인

만약 coins = [2, 3, 5], m=30 이면

- 2: 2, 4, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30 -> 15개
- 3: 3, 6, 9, 12, 15, 18, 21, 24, 27, 30 -> 10개
- 5: 5, 10, 15, 20, 25, 30 -> 6개

총 31개. 근데 겹치는 숫자들이 존재 -> {2}, {3}, {5}, {2,3}, {2,5}, {3,5}, {2,3,5} 에서 요소가 홀수개인건 더해주고, 짝수개인건 빼주면됨

=> m / 2 + m / 3 + m / 5 - m / 6 - m / 10 - m / 15 + m / 30 = (15 + 10 + 6) - (5 + 3 + 2) + 1 = 22

따라서 m(여기서는 30)까지 중복없이 등장하는 숫자의 개수는 22개

이를 함수로 나타내자면 count(30)=22, count(10)=8임

최종적으로 원하는 것은 k번째 숫자가 뭔지 구하는거임 (count(m) >= k)

따라서 답의 최대값 경계는 min(coins) * k 임 -> 가장 작은 동전을 k개 사용하면 가장 큰 k가 나오고 그보다 큰 숫자들이 사이사이에 값을 채우기에 실질적인 값은 해당 값보다 작아지게됨

ex) coins = [5, 2] k=7 이라면 2만 써도 7개의 금액을 만들 수 있으므로, 7번째 정답은 무조건 14 이하이고, 다른 동전 5가 중간에 5와 15를 추가하므로 실제 7번째 값은 더 앞당겨져 12가 되는것

따라서 left=1, right=min(coins)*k 로 해서 이분탐색을 진행.

count(mid) 값이 k보다 작다면 left+1, k보다 크다면 right=mid로 진행하고 left==right==count(mid) 라면 해당 값이 정답임.

---

이런 생각은 어떻게 하는거지? 대단;;
### 알고리즘
- 포함 - 배제
- 이분 탐색

### 시간복잡도:

### 공간복잡도:

## 다른사람들의 개쩌는답
