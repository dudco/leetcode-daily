## [841. Keys and Rooms](https://leetcode.com/problems/keys-and-rooms/description/?envType=study-plan-v2&envId=leetcode-75)

### 문제 설명
There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.

When you visit a room, you may find a set of distinct keys in it. Each key has a number on it, denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.

Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, return true if you can visit all the rooms, or false otherwise.

 

Example 1:
- Input: rooms = [[1],[2],[3],[]]
- Output: true
- Explanation: 
    
    We visit room 0 and pick up key 1.
    
    We then visit room 1 and pick up key 2.
    
    We then visit room 2 and pick up key 3.
    
    We then visit room 3.
    
    Since we were able to visit every room, we return true.

Example 2:
- Input: rooms = [[1,3],[3,0,1],[2],[0]]
- Output: false
- Explanation: We can not enter room number 2 since the only key that unlocks it is in that room.

Constraints:
- n == rooms.length
- 2 <= n <= 1000
- 0 <= rooms[i].length <= 1000
- 1 <= sum(rooms[i].length) <= 3000
- 0 <= rooms[i][j] < n
- All the values of rooms[i] are unique.

## 해석 및 풀이 방식
0번째 방에 접근 후 키를 각각 큐에 삽입, 큐가 빌 때 까지 pop 하면서 방을 이동하면됨.

해당 방에 접근하면 룸에 접근 했다고 데이터를 update 해줌.

만약 이미 접근했던 방이면 다시 갈 필요가없으니 무시해도됨

### 알고리즘


### 시간복잡도: O(n)

### 공간복잡도: O(1)
저장하는 문자가 소문자 26자 고정이기때문에 공간복잡도는 O(1)

## 다른사람들의 개쩌는답
