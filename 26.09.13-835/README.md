## [835. Image Overlap](https://leetcode.com/problems/image-overlap/description/?envType=daily-question&envId=2026-09-13)

**난이도:** 🟡 Medium

### 문제 설명
You are given two images, img1 and img2, represented as binary, square matrices of size n x n. A binary matrix has only 0s and 1s as values.

We translate one image however we choose by sliding all the 1 bits left, right, up, and/or down any number of units. We then place it on top of the other image. We can then calculate the overlap by counting the number of positions that have a 1 in both images.

Note also that a translation does not include any kind of rotation. Any 1 bits that are translated outside of the matrix borders are erased.

Return the largest possible overlap.

Example 1:
![](https://assets.leetcode.com/uploads/2020/09/09/overlap1.jpg)

- Input: img1 = [[1,1,0],[0,1,0],[0,1,0]], img2 = [[0,0,0],[0,1,1],[0,0,1]]
- Output: 3
- Explanation: We translate img1 to right by 1 unit and down by 1 unit.
    ![](https://assets.leetcode.com/uploads/2020/09/09/overlap_step1.jpg)
    The number of positions that have a 1 in both images is 3 (shown in red).
    ![](https://assets.leetcode.com/uploads/2020/09/09/overlap_step2.jpg)

Example 2:
- Input: img1 = [[1]], img2 = [[1]]
- Output: 1

Example 3:
- Input: img1 = [[0]], img2 = [[0]]
- Output: 0

Constraints:
- n == img1.length == img1[i].length
- n == img2.length == img2[i].length
- 1 <= n <= 30
- img1[i][j] is either 0 or 1.
- img2[i][j] is either 0 or 1.

## 해석 및 풀이 방식
1. 현재 위치에서 비교
2. BFS 마냥 오른쪽, 아래, 왼쪽, 위로 이동 후 비교
3. 만약 img1 이 전부 0으로 채워져버리면 더이상 옮기면 안됨
4. 만약 img2의 1의 개수와 동일한수가 나오면 그게 최대임

---

이미 체크해본 케이스는 무시하도록해야함. 어떻게하지?

---

비트연산으로 할걸 그랬나?

---
BFS 할 필요없고 그냥 오른쪽으로 쭉보고 한칸내리고, 다시 오른쪽으로 쪽보고 한칸내리고 반복

근데 연산횟수를 줄이기위해 비트연산을 이용함

대략적인 생각으로 img1의 1의 모양을 기준으로 찾아내는 방법도 있을 것 같음
### 알고리즘
- 비트 연산

### 시간복잡도: O(4 * N^3)

### 공간복잡도: O(N)

## 다른사람들의 개쩌는답
https://leetcode.com/problems/image-overlap/solutions/8518376/1-by-leetciub-fsnz/?envType=daily-question&envId=2026-09-13

3가지 방안을 소개해줌

방법1. 실제로 이동하고 세기
방법2. 이미지1과 이미지2에서 1이 위치하는 좌표를 세고, 좌표를 얼마나 이동하면되는지 확인한 뒤, 가장 많이 등장하는 이동좌표의 개수가 최대개수
방법3. Convolution.. 인데 이건 좀 어렵다