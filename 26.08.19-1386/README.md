## [1386. Cinema Seat Allocation](https://leetcode.com/problems/cinema-seat-allocation/description/?envType=daily-question&envId=2026-08-19)

### 문제 설명
A cinema has n rows of seats, numbered from 1 to n. Each row has 10 seats, numbered from 1 to 10.

You are given a 2D integer array reservedSeats, where reservedSeats[i] = [rowi, seati] means that seat seati in row rowi is already reserved.

A four-person group must be assigned to four seats in the same row. The group can be seated in one of the following seat blocks:

- seats 2, 3, 4, 5
- seats 4, 5, 6, 7
- seats 6, 7, 8, 9
A block can be used only if none of its seats are reserved. Each seat can be assigned to at most one group.

Return an integer denoting the maximum number of four-person groups that can be assigned.

Example 1:
- Input: n = 3, reservedSeats = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]
- Output: 4
- Explanation: The figure above shows an optimal allocation of four groups. Seats marked in blue are already reserved, and each set of four contiguous seats marked in orange is assigned to one group.

Example 2:
- Input: n = 2, reservedSeats = [[2,1],[1,8],[2,6]]
- Output: 2

Example 3:
- Input: n = 4, reservedSeats = [[4,3],[1,4],[4,6],[1,7]]
- Output: 4 

Constraints:
- 1 <= n <= 10^9
- 1 <= reservedSeats.length <= min(10 * n, 104)
- reservedSeats[i] == [rowi, seati]
- 1 <= rowi <= n
- 1 <= seati <= 10
- All reservedSeats[i] are distinct.

## 해석 및 풀이 방식
각 행을 돌면서 2, 3, 4, 5 / 4, 5, 6, 7 / 6, 7, 8, 9 가 가능한지 확인한다 -> O(10 * N) 으로 가능 : N개의 행을 각각 확인하는 방식 (최대 O(10^9))

모든 행은 기본적으로 2개의 좌석이 가능함. (2, 3, 4, 5), (6, 7, 8, 9) -> 아무것도 예약되어있지안다면 가능한 좌석 = n * 2

예약된 좌석에 따라 어떨 때 -1을 해주고, 어떨 때 -1을 안하면 상황에 따라서 +1을 해줘야할 때도 있을 것 같음

예약으로 들어온 좌석이 2, 3, 4, 5, 6, 7, 8, 9 중 하나면 확인을 해줘야함. 1, 10은 상관이없음 그대로 둬도됨

2,3,8,9가 들어왔고 2,3,8,9 모두 예약되어있지않으며 4,5,6,7이 비어있음 -> 가운데 좌석가능 -> -1
4,5이 들어왔고 4,5 모두 예약되어있지 않으며 6,7,8,9가 비어있음 -> 오른쪽 가능 -> -1 (근데 2,3이 먼저 채워져있었다면 이미 -1 되었으니 skip)
6,7이 들어왔고 6,7 모두 예약되어있지 않으며 2,3,4,5가 비어있음 -> 왼쪽 가능 -> -1 (근데 8,9가 먼저 채워져있었다면 이미 -1 되었으니 skip)

2, 3 이라면 왼쪽 좌석 사용 불가 -> 오른쪽 좌석 또는 가운데 좌석 사용가능 -> 4, 5가 체크되어있지 않음 -> 왼쪽좌석 막힌적 없음 -> -1

8, 9 이라면 오른쪽 좌석 사용불가 -> 왼쪽 좌석 또는 가운데 좌석 사용 가능 -> 6, 7가 체크되어있지 않음 -> 오른쪽좌석 막힌적 없음 -> -1

4, 5 이라면 왼쪽, 가운데 좌석 사용불가 -> 오른쪽 좌석 사용 가능 -> 2, 3가 체크되어있지 않음 -> 왼쪽좌석 막힌적 없음 -> -1

6, 7 이라면 오른쪽, 가운데 좌석 사용 불가 -> 왼쪽 좌석 사용 가능 -> 8, 9가 체크되어있지 않ㅇ므 -> 오른쪽좌석 막힌적 없음 -> -1

는 위와 같이하면 답이없음. 경우의수가 너무많음. 차라리 모든 좌석에 대해서 비트로 표시하고 가능한 좌석을 비트연산으로 확인한 뒤 더해주면됨

### 알고리즘

- 비트연산
- 해시테이블

### 시간복잡도: O(R)

예약된 좌석의 개수 R 만큼돌고, 해시맵의 크기는 R보다 클 수 없음 따라서 O(2 * R) -> O(R)

### 공간복잡도: O(R)

해시맵에 저장할 개수 O(R)

## 다른사람들의 개쩌는답
https://leetcode.com/problems/cinema-seat-allocation/editorial/?envType=daily-question&envId=2026-08-19

leetcode solution 인데 비트연산을 어떻게하는지 보면 나쁘지않음

left, middle, right = 0b11110000, 0b11000011, 0b00001111 # 왼쪽 좌석, 가운데 좌석, 오른쪽좌석 표시해두고

occupied[seat[0]] |= 1 << (seat[1] - 2) # 예약된 좌석 표시 (-2는 8자리 좌석으로 맞추기위해 1, 10번은 어차피 어디에나 가능함)

(bitmask | left) == left or (bitmask | middle) == middle or (bitmask | right) == right # row와 좌석들을 or연산해서 좌석이 나옴 -> 그룹가능 -> +1

내꺼랑 다른건 기존에 1번, 10번이 나올 가능성을 없애버려서 해시맵에서 2개의 좌석이 나올 확률을 없앰 -> 따라서 if문 하나로도 처리가 가능하고 해시맵 반복문을 조금이라도 줄임
