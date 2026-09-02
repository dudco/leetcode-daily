## [605. Can Place Flowers](https://leetcode.com/problems/can-place-flowers/description/?envType=study-plan-v2&envId=leetcode-75)

### 문제 설명
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

Example 1:
- Input: flowerbed = [1,0,0,0,1], n = 1
- Output: true

Example 2:
- Input: flowerbed = [1,0,0,0,1], n = 2
- Output: false

Constraints:
- 1 <= flowerbed.length <= 2 * 10^4
- flowerbed[i] is 0 or 1.
- There are no two adjacent flowers in flowerbed.
- 0 <= n <= flowerbed.length
## 해석 및 풀이 방식
앞에서 부터 진행하면서 만약 채울 수 있으면 그냥 바로 채워주는 방식으로 처리해주면 될듯

현재 위치의 값이 0임 -> 앞에서부터 진행하면서 왔으니 만약 채울 수 없었다면 현재 위치는 1또는 2가 있었을 것임 -> 따라서 다음것이 0이면 채울 수 있음 -> 근데 만약 다음이 없다면? 그냥 채우면됨

현재 위치의 값이 1임 -> -1, +1 부분을 2로 변경

현재 위치의 값이 2임 -> 이전 것에 의해서 변경된거임 그냥 두면됨

### 알고리즘

- 그냥 앞에서부터 순차탐색 ..

### 시간복잡도: O(N)

### 공간복잡도: O(1)

## 다른사람들의 개쩌는답
https://leetcode.com/problems/can-place-flowers/solutions/127632/can-place-flowers-by-leetcode-u41p/?envType=study-plan-v2&envId=leetcode-75

굳이 2로 바꿀 필요는 없었고, 현재 위치의 값이 0이다? 그러면 앞, 뒤 확인만하면됨. 만약 둘 다 비어있다면 해당 부분을 1로 업데이트 업데이트하면서 cnt값 + 1 하고 cnt값이 최종적으로 n보다 큰지만 확인하면됨
