## [1493. Longest Subarray of 1's After Deleting One Element](https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/?envType=study-plan-v2&envId=leetcode-75)

### 문제 설명
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

Example 1:
- Input: nums = [1,1,0,1]
- Output: 3
- Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.

Example 2:
- Input: nums = [0,1,1,1,0,1,1,0,1]
- Output: 5
- Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].

Example 3:
- Input: nums = [1,1,1]
- Output: 2
- Explanation: You must delete one element.

Constraints:
- 1 <= nums.length <= 10^5
- nums[i] is either 0 or 1.
## 해석 및 풀이 방식
단 하나의 element를 지울 때 어디를 제거해야 가장 긴 1로만 이루어진 부분수열을 만들 수 있는지 묻는 문제. 무조건 하나를 지워야함

1. 맨 처음 1이 나오는 순간 몇개가 나오는지 기록. (앞쪽의 0의 개수는 어차피 1개만 바꾼다고할 때 +1만 되므로 의미가없음)
2. 이후 0이 처음으로 나오는 순간 해당 0을 변경하지 않을 때와 변경할 때의 방식 처리
3. 다시 1이 나오는 개수 센 뒤 다음 0 다시 시도.

---

1. 1이 나오는 구간들을 tuple로 구성
2. tuples[i] 의 tuple[1] - tuple[0] 이 ret보다 크다면 tuple[1] - tuple[0] 기입
3. tuples[i]의 tuple[1]과 tuples[i+1] 의 tuple[0]이 1밖에 차이가 안난다 -> tuples[i] 와 tuples[i+1] 은 합칠 수 있음. -> tuples[i+1][1] - tuples[i][0] -1 을 ret으로 설정

### 알고리즘

### 시간복잡도: O(N + N/2)
- 전체 nums 를 검사 + 최악의 경우 1, 0이 반복해서 나옴
### 공간복잡도: O(N/2)
- 최악의 경우 1, 0이 반복해서 나올 때 N/2 개의 크기만큼 배열 필요

## 다른사람들의 개쩌는답
https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/solutions/7114750/sliding-window-java-c-c-c-python3-go-js-2rt8c/?envType=study-plan-v2&envId=leetcode-75

그냥 슬라이딩 윈도우 방식을 이용, 0을 만나면 0의 개수를 증가시켜주고, 항상 0의 개수가 하나만 존재하도록 처리해주면됨