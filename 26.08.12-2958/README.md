
## [2958. Length of Longest Subarray With at Most K Frequency](https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/description/?envType=daily-question&envId=2026-08-12)

### 문제 설명
You are given an integer array nums and an integer k.

The frequency of an element x is the number of times it occurs in an array.

An array is called good if the frequency of each element in this array is less than or equal to k.

Return the length of the longest good subarray of nums.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

- Input: nums = [1,2,3,1,2,3,1,2], k = 2
- Output: 6
- Explanation: The longest possible good subarray is [1,2,3,1,2,3] since the values 1, 2, and 3 occur at most twice in this subarray. Note that the subarrays [2,3,1,2,3,1] and [3,1,2,3,1,2] are also good.

It can be shown that there are no good subarrays with length more than 6.

Example 2:

- Input: nums = [1,2,1,2,1,2,1,2], k = 1
- Output: 2
- Explanation: The longest possible good subarray is [1,2] since the values 1 and 2 occur at most once in this subarray. Note that the subarray [2,1] is also good.

It can be shown that there are no good subarrays with length more than 2.

Example 3:

- Input: nums = [5,5,5,5,5,5,5], k = 4
- Output: 4
- Explanation: The longest possible good subarray is [5,5,5,5] since the value 5 occurs 4 times in this subarray.

It can be shown that there are no good subarrays with length more than 4.
 

Constraints:

- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
- 1 <= k <= nums.length

## 해석 및 풀이 방식

증가하는 수열이 아닌 그냥 부분 수열 찾고 해당 부분수열을 이루는 값들의 빈도수를 체크해야함. 

근데 이거 빈도수만 맞으면 되니 1,2,3,1,2,3 뿐만아니라 1,2,3,3,2,1도 가능함.

으으으음 어떻게 접근해야할까아 -> Sliding window가 가장 쉬워보임.

0,0에서 시작하는 sliding window 에서 하나씩 증가시키면서 진행.

왼쪽부터 진행하면서 엘리먼트 개수를 세고, 만약 element 개수를 초과하는 경우가 나오면 왼쪽 포인터 증가시키는 방식으로 진행.

만약 최대 엘리먼트 개수까지 도달한다면 그것보다 큰 건 없으니 그냥 거기서 끝내버리면됨 -> 이건아님 가장 긴 수열을 찾아야하기에 전체를 다 돌아봐야함.

만약 모든 엘리먼트 개수가 최대라면? -> 이것도 애매한 1,2,3,1,2,3 다음에 1,2,3,1,2,3,5,5가 나올수도있으니 다음것도 찾아야함

왼쪽, 오른쪽 포인터를 두고 현재 오른쪽 포인터에 있는 값이 몇개있는지 해시테이블에서 조회

만약 해당값이 k보다 작다면 해당 값을 1증가시키고 오른쪽 포인터 오른쪽으로 한칸 이동. 반복

만약 해당값이 k보다 크거나 같다면 왼쪽 포인터에있는 값의 개수를 1감소시키고 왼쪽 포인터 오른쪽으로 한칸이동

### 알고리즘
Sliding Window + Hash Table

### 시간복잡도: O(n)
최악의 경우 왼쪽포인터 O(n) + 오른쪽 포인터 O(n) 이므로 O(2n) -> O(n) 의 시간을 가짐

### 공간복잡도: O(n)
해시 테이블 데이터를 저장할 공간이 필요하니 O(n)의 공간복잡도를 가짐

## 다른사람들의 개쩌는답
거의 다 답이 비슷함. 근데 사람들은 C++로 풀어서 속도가 빠른듯. 