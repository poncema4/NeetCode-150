from typing import List
from collections import deque

class Solution:
    def grid_path(self, n: int, m: int, obstacles: List[List[int]], teleports: List[List[int]]) -> int:
        """
        Start at the top-left corner (0, 0) and have your goal be the bottom-right corner (n - 1, m - 1) in a grid,
        considering obstacles and teleports. 

        Obstacles --> A grid cell that cannot be entered
        Teleports --> Move you from one cell to another

        Use breadth-first search to track the shortest distance while only being able to move right, if not possible
        then return -1
        """
        obstacle_set = set((r, c) for r, c in obstacles)

        teleport_map = {}
        for r1, c1, r2, c2 in teleports:
            teleport_map[(r1, c1)] = (r2, c2)

        queue = deque([(0, 0, 0)])
        visited = set([(0, 0)])

        while queue:
            r, c, dist = queue.popleft()
            if r == n - 1 and c == m - 1:
                return dist
            
            if (r, c) in teleport_map:
                tr, tc = teleport_map[(r, c)]
                if (tr, tc) not in visited and (tr, tc) not in obstacle_set:
                    visited.add((tr, tc))
                    queue.append((tr, tc, dist))

            nr, nc = r, c + 1
            if (0 <= nr < n and 0 <= nc < m and (nr, nc) not in obstacle_set and (nr, nc) not in visited):
                visited.add((nr, nc))
                queue.append((nr, nc, dist + 1))

        return -1
    
c = Solution()
n = 1
m = 20
obstacles = [[0, 5], [0, 10], [0, 15]]
teleports = [[0, 4, 0, 6], [0, 9, 0, 11], [0, 14, 0, 16]]
print(c.grid_path(n, m, obstacles, teleports))