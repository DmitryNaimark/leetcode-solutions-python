# https://leetcode.com/problems/number-of-closed-islands/
# ---------------------------------------------------
from typing import List
from collections import deque

# Runtime Complexity: O(m*n)
# Space Complexity: O(m*n) in worst case. Buts, realistically it's better than in recursive approach,
#     since we would remove the cell from the stack before adding its neighbors.
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        # If grid is empty
        if not any(grid):
            return 0

        rows, cols = len(grid), len(grid[0])

        def dfs_fill(r, c, val):
            q = deque()
            q.append((r, c))

            while q:
                cr, cc = q.pop()

                grid[cr][cc] = val
                for dr, dc in ((-1, 0), (0, 1), (1, 0), (0, -1)):
                    if 0 <= cr + dr < rows and 0 <= cc + dc < cols and grid[cr + dr][cc + dc] != val:
                        q.append((cr + dr, cc + dc))

        # Since edges can't be islands, fill them and their neighbors with 1 recursively.
        for r in range(rows):
            for c in range(cols):
                if (r == 0 or r == rows - 1 or c == 0 or c == cols - 1) and grid[r][c] == 0:
                    dfs_fill(r, c, 1)

        res = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    res += 1
                    dfs_fill(r, c, 1)

        return res

# ---------------------------------------------------
#                    Test Cases
# ---------------------------------------------------
solution = Solution()
# 2
print(solution.closedIsland([
    [1, 1, 1, 1, 1, 1, 1, 0],
    [1, 0, 0, 0, 0, 1, 1, 0],
    [1, 0, 1, 0, 1, 1, 1, 0],
    [1, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 0]]))

# 1
print(solution.closedIsland([
    [0, 0, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 1, 1, 0]]))

# 2
print(solution.closedIsland([
    [1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1]]))
