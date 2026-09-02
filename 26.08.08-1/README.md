## 1. [Two Sum](https://leetcode.com/problems/two-sum/description/)

### 문제 설명
You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

## 해석 및 풀이 방식
10^4 밖에 안되니 그냥 완전탐색을 해도됨

근데 더 좋은 방식은 정렬 후 투포인터 이용해도 괜찮을듯?

1. 정렬
2. 왼쪽 포인터 + 오른쪽 포인터의 값이 target 보다 크다? (sum - target > 0) -> 오른쪽 포인터 한칸 왼쪽으로
3. 왼쪽 포인터 + 오른쪽 포인터의 값이 target 보다 작다? (sum - target < 0) -> 왼쪽 포인터 한칸 오른쪽으로

는 원래 위치를 반환해줘야함. -> 정렬해서 찾은 뒤 원래 위치 반환
는 같은 숫자 두개만 들어오면 오류남. -> l의 원래위치보다 한개 증가한 뒤 숫자를 찾게함 (이건안됨) -> 앞쪽부터는 index로 찾고 뒤쪽부터는 그냥 배열 순회해서 찾은 뒤 작은값은 첫번째, 큰값은 두번째 엘리먼트로 반환

### 알고리즘
- 정렬
- 투포인터

### 시간복잡도: O(nlogn)

### 공간복잡도: O(n)

## 다른사람들의 개쩌는답
1. https://leetcode.com/problems/two-sum/solutions/3619262/3-methods-c-java-python-beginner-friendl-x595/

그냥 해시태이블로하네..