## [2213. Longest Substring of One Repeating Character](https://leetcode.com/problems/longest-substring-of-one-repeating-character/description/?envType=daily-question&envId=2026-08-13)

### 문제 설명
You are given a 0-indexed string s. You are also given a 0-indexed string queryCharacters of length k and a 0-indexed array of integer indices queryIndices of length k, both of which are used to describe k queries.

The ith query updates the character in s at index queryIndices[i] to the character queryCharacters[i].

Return an array lengths of length k where lengths[i] is the length of the longest substring of s consisting of only one repeating character after the ith query is performed.

 

Example 1:
- Input: s = "babacc", queryCharacters = "bcb", queryIndices = [1,3,3]
- Output: [3,3,4]
- Explanation: 
    
    - 1st query updates s = "bbbacc". The longest substring consisting of one repeating character is "bbb" with length 3.
    
    - 2nd query updates s = "bbbccc". 
    
    The longest substring consisting of one repeating character can be "bbb" or "ccc" with length 3.
    
    - 3rd query updates s = "bbbbcc". The longest substring consisting of one repeating character is "bbbb" with length 4.
    
    Thus, we return [3,3,4].

Example 2:
- Input: s = "abyzz", queryCharacters = "aa", queryIndices = [2,1]
- Output: [2,3]
- Explanation:
    
    - 1st query updates s = "abazz". The longest substring consisting of one repeating character is "zz" with length 2.

    - 2nd query updates s = "aaazz". The longest substring consisting of one repeating character is "aaa" with length 3.
    
    Thus, we return [2,3].
 

Constraints:
- 1 <= s.length <= 10^5
- s consists of lowercase English letters.
- k == queryCharacters.length == queryIndices.length
- 1 <= k <= 10^5
- queryCharacters consists of lowercase English letters.
- 0 <= queryIndices[i] < s.length

## 해석 및 풀이 방식
문자열 자체가 최대 100,000 / k도 100,000 이라 꽤 큼

업데이트 자체는 특정 인덱스를 변경하는 것이기 때문에 O(1)이고 다시 되돌릴 필요도 없기에 그냥하면되는데 한번 업데이트 때 마다 문자열을 계속해서 검사하면 최대 O(N*M) 이기에 너무 오래걸림

세그먼트 트리! - 여러개의 데이터가 연속적으로 존재할 때 특정 범위의 값을 가장 빠르게 구하는 방법임

5개의 엘리먼트가 있다면
```
             A[0:4]
      A[0:2]      A[3:4]
  A[0:1]  A[2:2]  A[3:3] A[4:4]
A[0:0]A[1:1]
```
위와 같은 구조를 가지는 트리를 세그먼트 트리라고함

- 문제점1. 세그먼트 트리 업그레이드 시 몇번째를 바꿔야하는지 계산해야함 -> 문자열이 얼마나 슬라이스 되었을 때 idx 값이 변경되어야할까? -> start 만큼 빼주면됨
```
# 첫번째 문자열 그대로 -> 크기 6 -> idx=1 은 6보다 작으니 그대로
# 두번째 문자열 반갈 -> 왼쪽: [0:2] / 오른쪽: [3:5] -> idx=1 은 3보다 작으니 그대로
# 세번째 문자열 반갈 -> 왼쪽: [0:1], 오른쪽: [2:2] -> idx=1 start < idx < end 이므로 그대로
# 네번째 문자열 반갈 -> 왼쪽: [0:0], 오른쪽: [1:1] -> idx - start
```
- 문제점2. 가장 긴걸 어떻게 찾을까? -> 그냥 트리 내려가면서 가장 긴 문자열을 찾고, 해당 위치의 배열의 친척(sibiling)을 검사하면됨
```
만약 1이면 -> [1] -> 친척 x
만약 2이면 -> [2:3] -> 얘는 이전거는 확인하면 안됨
만약 3이면 -> [2:3] -> 얘는 다음거는 확인하면 안됨
만약 4이면 -> [4:7] -> 얘는 이전거는 확인하면 안됨
만약 5이면 -> [4:7]
만약 6이면 -> [4:7] 
만약 7이면 -> [4:7] -> 얘는 다음거는 확인하면 안됨
만약 8이면 -> [8:15] -> 얘는 이전거는 확인하면 안됨
...
만약 15이면 -> [8:15] -> 얘는 다음거는 확인하면 안됨
```
    
    -> 1, 2, 4, 8, 16, 32, 64 같은 얘들은 이전거 확인하면 안됨 -> 2^n은 이전거 확인하면 안됨

    ->    1, 3, 7, 15, 31, 63 같은 애들은 다음거 확인하면 안됨 -> 2^n-1은 다음거 확인하면 안됨

- 문제점3: 전체를 다 돌 필요는 없음
```
만약 1이 다 같음 -> 1만 확인하면 됨 -> 1
만약 2~3 중 같은게 있음 -> 2, 3만 확인하면됨 -> 2
만약 4~7 중 같은게 있음 -> 4~8만 확인하면됨 -> 4
만약 8~15 중 같은게 있음 -> 8~15만 확인하면됨 -> 8
만약 16~31 중 같은게 있음 -> 16~31만 확인하면됨 -> 32
```
1부터 1 -> 2~3 -> 4~7 -> 8~16 확인하는 식으로 로직을 바꾸는게 좋을듯

-> 직접 해보니 예외가 있음 -> 가장 마지막 depth - 1 의 경우 중간중간 비어있는 애들, 1개로만 있는 애들이 있음 -> 상황에 따라 ge / eb 로 나눠져있고 홀수라서 마지막에 한개밖에없으면 1로 처리될 가능성이 있음

-> 예외처리? or 다음 depth 까지만 진행해보기

- 문제점4: 57번째에서 같은애들 발견 -> 58도 다 같음 -> 59까지 확인해야함

- 문제점5: 결국 문제가 되는 순간 -> abb + bba 이 경우 무조건 아래까지 내려가봐야함

-> 걍 맨 아래에서 찾아버리면 되는거 아님?

-> 차라리 2**tree_height ~ (2**tree_height - 1 * 2 - 1) 구간에서 찾기 -> 안되네;;'

- Hint 1
    
    Use a segment tree to perform fast point updates and range queries.
- Hint 2
    
    We need each segment tree node to store the length of the longest substring of that segment consisting of only 1 repeating character.
- Hint 3
    
    We will also have each segment tree node store the leftmost and rightmost character of the segment, the max length of a prefix substring consisting of only 1 repeating character, and the max length of a suffix substring consisting of only 1 repeating character.
- Hint 4
    
    Use this information to properly merge the two segment tree nodes together.

### 알고리즘
세그먼트 트리

- 결국 힌트를 이용했다. 

- 정답은 그냥 트리 만들고, 업데이트할 때 바로바로 고쳐주는 것이었다.

- 굳이 트리 만들고 계산하는것보다 재귀적으로 쭉~ 들어간 뒤에 업데이트해주면 되는 트리들만 찾아서 업데이트해주는 방식.

### 시간복잡도: O(n + q * logn)

### 공간복잡도: O(n)

## 다른사람들의 개쩌는답
https://leetcode.com/problems/longest-substring-of-one-repeating-character/solutions/8457810/100-hard-problem-with-easy-approach-6-la-5ri6/?envType=daily-question&envId=2026-08-13

어프로치는 동일한데 조금 더 읽기 쉽고 두 부분정도 최적화 되어있음

1. update 시 굳이 가 볼 필요없는 곳은 재귀로 들어가지조차않음.

2. 전체가 한글자로 만들어져있는지 확인하는 로직이 나보다 간결함

    1. 접두사 길이는 기본적으로 왼쪽 노드의 접두사 길이

    2. 왼쪽 노드의 끝 글자 == 오른쪽 노드의 시작글자 && 왼쪽 노드의 접두사의 길이 == 왼쪽 노드 원본 문자열의 길이 -> 해당 노드의 접두사의 길이 = 왼쪽 노드 원본 문자열 길이 + 오른쪽 노드 접두사

    3. 왼쪽 노드의 끝 글자 == 오른쪽 노드의 시작글자 && 오른쪽 노드의 접미사의 길이 == 오른쪽 노드 원본 문자열의 길이 -> 해당 노드의 접미사의 길이 = 오른쪾 노드 원본 문자열 길이 + 왼쪽 노드 접미사

https://leetcode.com/problems/longest-substring-of-one-repeating-character/solutions/8457838/10-ms-using-two-ordered-sets-and-frequen-21ve

Segment Tree를 이용하지 않고 Ordered Set을 이용하는 방식

1. 앞쪽부터 쭉 돌면서 문자가 달라지는 경계위치를 찾고 -> 빠르게 경계를 추가하기 위해서도 Ordered Set 사용

2. 문자를 바꾸면 그 주변의 경계만 추가, 삭제하고 영향 받는 구간 길이들의 개수를 갱신 -> 이 때 가장 가까운 주변 경계를 빠르게 찾기 위해 Ordered Set을 이용

3. 마지막으로 가장 긴 반복 문자열 길이를 얻는 방식

이렇게하면 시간복잡도를 O(N + K) 로 할 수 있음