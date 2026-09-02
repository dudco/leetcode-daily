## [3720. Lexicographically Smallest Permutation Greater Than Target](https://leetcode.com/problems/lexicographically-smallest-permutation-greater-than-target/description/?envType=daily-question&envId=2026-08-27)

### 문제 설명
You are given two strings s and target, both having length n, consisting of lowercase English letters.

Return the lexicographically smallest permutation of s that is strictly greater than target. If no permutation of s is lexicographically strictly greater than target, return an empty string.

A string a is lexicographically strictly greater than a string b (of the same length) if in the first position where a and b differ, string a has a letter that appears later in the alphabet than the corresponding letter in b.

Example 1:
- Input: s = "abc", target = "bba"
- Output: "bca"
- Explanation:
    
    The permutations of s (in lexicographical order) are "abc", "acb", "bac", "bca", "cab", and "cba".
    
    The lexicographically smallest permutation that is strictly greater than target is "bca".

Example 2:
- Input: s = "leet", target = "code"
- Output: "eelt"
Explanation:
    
    The permutations of s (in lexicographical order) are "eelt", "eetl", "elet", "elte", "etel", "etle", "leet", "lete", "ltee", "teel", "tele", and "tlee".
    
    The lexicographically smallest permutation that is strictly greater than target is "eelt".

Example 3:
- Input: s = "baba", target = "bbaa"
- Output: ""
- Explanation:
    
    The permutations of s (in lexicographical order) are "aabb", "abab", "abba", "baab", "baba", and "bbaa".
    
    None of them is lexicographically strictly greater than target. Therefore, the answer is "".

Constraints:
- 1 <= s.length == target.length <= 300
- s and target consist of only lowercase English letters.

## 해석 및 풀이 방식
맨 앞 타겟부터 시작해서 target i보다 큰 source 문자 찾기 -> target 보다 작은 문자열을 찾을 순 있지만 만들 수 있는 문자열 중 가장 작은 문자열은 아님

source 문자열로 만들 수 있는 모든 문자열을 처리해야하나?
---
Maintain frequency counts of s.

Walk left-to-right; if equal to target[i] is possible, take it and continue.

If not, try the smallest letter strictly greater than target[i].

If neither, backtrack left to the most recent index where you matched target and try to bump there.
---
source 문자열에 target[i] 보다 큰 문자가 나타나면 해당 부분을 해당문자열로 바꾸고 나머지는 정렬 순서대로 이어주면됨

source 문자열에 target[i] 보다 큰 문자가 안나타나면 해당 부분과 같은 문자열이라도 채택, 다음 문자열 진행
---
1. target[i] 보다 큰 source가 존재 -> i+1 부터는 뭐가오든 target 보다 커짐

2. target[i] 와 같은 source가 존재 -> i+1 에는 같거나 큰게 와야함

3. 1,2 다 없음 -> 불가능
---
근데 목표는 결과적으로 가장작은 문자열을 찾는것임 그래서 큰게있는지 검사하는것보다 같은게 있는지 먼저 검사
1. target[i] 와 같은 source 가 존재 -> 채택 후 다음 문자열 검사 시작

2. 쭉 가다가 맨 마지막 문자임. 해당 문자는 마지막 target 보다는 무조건 커야함. 안그럼 같은 문자임으로 lexicographically strictly greater가 안됨

3. 만약 return 되었을 때 값이 ""가 아니다 -> 그것이 답임 바로 리턴

4. 만약 return 되었을 때 값이 ""다 -> 해당 위치에서는 같은걸 사용했을 때 가능한 경우가 없다 -> 더 큰게 있는지 확인해서 큰걸로 채택해서 위 로직 반복

근데 이렇게하면 시간이 너무오래걸림 -> 최대 시간 300개를 다 확인해야하기때문

그래서 hash 테이블로 영문자가 몇번 등장하는지 미리 저장, 해당 해시테이블을 이용하여 

그러면 최대 반복문이 26번밖에 안되기때문
---
### 알고리즘
- hash table
- greedy

### 시간복잡도: O(N + N*N)

### 공간복잡도: O(1)

## 다른사람들의 개쩌는답
