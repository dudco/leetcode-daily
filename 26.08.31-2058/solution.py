# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: ListNode | None) -> list[int]:
        p = c = n = None
        p = head # 이전
        c = head.next # 현재
        if c is not None and c.next is not None:
            n = c.next # 다음

        firstCriticalPointIdx = -1
        lastCriticalPointIdx = -1

        idx = 1

        minDistance = -1
        maxDistance = -1

        while n is not None:
            if c.val > p.val and c.val > n.val:
                # critical point
                if firstCriticalPointIdx == -1:
                    firstCriticalPointIdx = idx
                    lastCriticalPointIdx = idx
                else:
                    if minDistance != -1:
                        minDistance = min(minDistance, idx - lastCriticalPointIdx)
                    else:
                        minDistance = idx - lastCriticalPointIdx
                    maxDistance = idx - firstCriticalPointIdx
                    lastCriticalPointIdx = idx
            elif c.val < p.val and c.val < n.val:
                # cretical point
                if firstCriticalPointIdx == -1:
                    firstCriticalPointIdx = idx
                    lastCriticalPointIdx = idx
                else:
                    if minDistance != -1:
                        minDistance = min(minDistance, idx - lastCriticalPointIdx)
                    else:
                        minDistance = idx - lastCriticalPointIdx
                    maxDistance = idx - firstCriticalPointIdx
                    lastCriticalPointIdx = idx
            p = c
            c = n
            n = n.next
            idx += 1

        return [minDistance, maxDistance]
