## [1448. Count Good Nodes in Binary Tree](https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/?envType=study-plan-v2&envId=leetcode-75)

### 문제 설명
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.

Return the number of good nodes in the binary tree.

Example 1:
- Input: root = [3,1,4,3,null,1,5]
- Output: 4
- Explanation: Nodes in blue are good.
    
    Root Node (3) is always a good node.
    
    Node 4 -> (3,4) is the maximum value in the path starting from the root.
    
    Node 5 -> (3,4,5) is the maximum value in the path
    
    Node 3 -> (3,1,3) is the maximum value in the path.

Example 2:
- Input: root = [3,3,null,4,2]
- Output: 3
- Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.
 

Constraints:
- The number of nodes in the binary tree is in the range [1, 10^5].
- Each node's value is between [-10^4, 10^4].

## 해석 및 풀이 방식
그냥 DFS 로 하는데 재귀로 들어갈 때 함수 맨 뒤에 자기 자신을 넣어서 보내면됨. 그리고 해당 배열 내에 자기 자신보다 큰 애가 없으면 + 1

### 알고리즘


### 시간복잡도: O(n)

### 공간복잡도: O(1)
저장하는 문자가 소문자 26자 고정이기때문에 공간복잡도는 O(1)

## 다른사람들의 개쩌는답
