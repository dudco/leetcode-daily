## [1510. Stone Game IV](https://leetcode.com/problems/smallest-divisible-digit-product-ii/description/?envType=daily-question&envId=2026-08-07)

### 문제 설명
Alice and Bob take turns playing a game, with Alice starting first.

Initially, there are n stones in a pile. On each player's turn, that player makes a move consisting of removing any non-zero square number of stones in the pile.

Also, if a player cannot make a move, he/she loses the game.

Given a positive integer n, return true if and only if Alice wins the game otherwise return false, assuming both players play optimally.

 
Example 1:

Input: n = 1

Output: true

Explanation: Alice can remove 1 stone winning the game because Bob doesn't have any moves.

Example 2:

Input: n = 2

Output: false

Explanation: Alice can only remove 1 stone, after that Bob removes the last one winning the game (2 -> 1 -> 0).

Example 3:

Input: n = 4

Output: true

Explanation: n is already a perfect square, Alice can win with one move, removing 4 stones (4 -> 0).
 

Constraints:

1 <= n <= 100,000

## 해석 및 풀이 방식
DP 방식으로 처리해야함. dp[i]가 True면 

### 알고리즘


### 시간복잡도: 


### 공간복잡도: 

## 다른사람들의 개쩌는답
