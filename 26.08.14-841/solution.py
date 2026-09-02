class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        visited = [False] * len(rooms)
        
        q = [*rooms[0]]
        visited[0] = True
        while(len(q) > 0):
            n = q.pop()

            if not visited[n]:
                visited[n] = True
                q.extend(rooms[n])

        return all(v for v in visited)