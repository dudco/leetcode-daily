## [104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/description/?envType=study-plan-v2&envId=leetcode-75)

### 문제 설명
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example 1:
- Input: root = [3,9,20,null,null,15,7]
- Output: 3

Example 2:
- Input: root = [1,null,2]
- Output: 2

 

Constraints:
- The number of nodes in the tree is in the range [0, 104].
- -100 <= Node.val <= 100

## 해석 및 풀이 방식
Binary Tree의 최대 깊이를 계산하는 문제

그냥 전체 배열 길이가 2의 몇승인지 찾으면됨 -> 2**n <= len(root)+1

n <= log2(len(root)+1)

---
근데 입력이 배열이 아니라 트리 노드로 주어짐;;

### 알고리즘


### 시간복잡도: O(n)

### 공간복잡도: O(1)
저장하는 문자가 소문자 26자 고정이기때문에 공간복잡도는 O(1)

## 다른사람들의 개쩌는답
