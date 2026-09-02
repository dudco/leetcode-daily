## [3875. Construct Uniform Parity Array I](https://leetcode.com/problems/construct-uniform-parity-array-i/description/?envType=daily-question&envId=2026-09-02)

### 문제 설명
You are given an array nums1 of n distinct integers.

You want to construct another array nums2 of length n such that the elements in nums2 are either all odd or all even.

For each index i, you must choose exactly one of the following (in any order):

nums2[i] = nums1[i]

nums2[i] = nums1[i] - nums1[j], for an index j != i

Return true if it is possible to construct such an array, otherwise, return false.

Example 1:
- Input: nums1 = [2,3]
- Output: true
- Explanation:

    Choose nums2[0] = nums1[0] - nums1[1] = 2 - 3 = -1.
    
    Choose nums2[1] = nums1[1] = 3.
    
    nums2 = [-1, 3], and both elements are odd. Thus, the answer is true​​​​​​​.

Example 2:
- Input: nums1 = [4,6]
- Output: true
- Explanation:​​​​​​​

    Choose nums2[0] = nums1[0] = 4.
    
    Choose nums2[1] = nums1[1] = 6.
    
    nums2 = [4, 6], and all elements are even. Thus, the answer is true.
 

Constraints:
- 1 <= n == nums1.length <= 100
- 1 <= nums1[i] <= 100
- nums1 consists of distinct integers.
## 해석 및 풀이 방식
nums2 배열을 만드는데 해당 배열은 nums1 의 해당 idx 또는 nums1의 해당 idx 와 다른 idx와의 차이로 만들어짐.

이 때 만들어진 num2 배열이 모두 홀수 혹은 짝수로 이뤄질 수 있다면 True / 아니라면 False 반환

1. num2 배열을 만들 때 해당 숫자가 홀수라면 특정 수를 뺏을 때 짝수가 만들어지는 상황이 생기는지 확인 -> 특정 수를 뺏을 때 전부 홀수인지 확인
2. num2 배열을 만들 때 해당 숫자가 짝수라면 특정 수를 뺏을 때 홀수가 만들어지는 상황이 생기는지 확인
-> 특정 수를 뺏을 때 전부 짝수인지 확인
3. 1.또는 2.가 만족되면 전체가 홀수 혹은 짝수로 이뤄질 수 있음
4. 특정 idx 에서 1.이 만족되지 않음 -> 해당 idx에 의해 전체가 홀수로만 이뤄져야함
5. 특정 idx 에서 2.이 만족되지 않음 -> 해당 idx에 의해 전체가 짝수로만 이뤄져야함
---
뭔가 맨 처음 n을 처리하고, 배열을 순회하면서 해당 n에 숫자를 연산해서 최종적으로 해당 idx에서 홀수만 가능한지, 짝수만 가능한지, 아님 모두 가능한지 판단해야할 것 같음

---
a	    b	 a - b
짝수	짝수	짝수
짝수	홀수	홀수
홀수	짝수	홀수
홀수	홀수	짝수

만약 배열 내에 홀수가 하나라도 존재함 -> 해당 홀수를 짝수에서 빼주면 전부 홀수로 변환 가능
만약 배열 내에 홀수가 하나도 없음 -> 전부 짝수 배열

### 알고리즘
- 수학
### 시간복잡도: O(1)

### 공간복잡도: O(1)

## 다른사람들의 개쩌는답
