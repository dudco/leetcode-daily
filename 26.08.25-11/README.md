## [11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/description/?envType=study-plan-v2&envId=leetcode-75)

### 문제 설명
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:
- Input: height = [1,8,6,2,5,4,8,3,7]
- Output: 49
- Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
- Input: height = [1,1]
- Output: 1

Constraints:
- n == height.length
- 2 <= n <= 10^5
- 0 <= height[i] <= 10^4

## 해석 및 풀이 방식
대표적인 투포인터 문제

l=0, r=n-1 일 때 채울 수 있는 물의 양을 계산, 기존것보다 많으면 해당 값으로 수정

물의 양 계산 방법 -> r - l * min(h[r], h[l])

그냥 단순히하면 안됨. 기본적으로 height[l] > height[r] 이라면 r을 하나씩 줄여주고, 반대라면 l을 1씩 증가시키는 방식으로 처리하면됨

짧은 쪽 포인터를 움직이는 이유는 다음과 같습니다.
- height[left] <= height[right]라고 가정합니다.
- 현재 left를 유지한 채 right만 줄이면, 가로 길이는 반드시 줄어듭니다.
- 물의 높이는 이미 height[left]를 넘을 수 없습니다. 
- 따라서 현재 left와 만들 수 있는 최대 넓이는 이미 현재 right와 계산한 넓이입니다.
- 그러므로 left는 더 이상 볼 필요가 없고, left += 1 합니다.
- 반대의 경우도 동일하게 right -= 1 하면 됩니다. 높이가 같은 경우에는 어느 한쪽을 옮겨도 되며, 위 코드는 왼쪽을 옮깁니다.

### 알고리즘

### 시간복잡도: O(N)

### 공간복잡도: O(1)

## 다른사람들의 개쩌는답
