# https://leetcode.com/problems/flood-fill/
# ---------------------------------------------------
from collections import deque
from typing import List

# Runtime Complexity: O(N), where N is the amount of same-colored neighbors
# Space Complexity: O(N) in worst case, if same-colored neighbors are in positioned as continuous line.
class Solution:
    # __init_ is created, so that there is no warning that self.* vars are defined outside of __init__ initially
    def __init__(self):
        self.rows = self.cols = 0
        self.color = None
        self.image = None

    def floodFill(self, image: List[List[int]], sr: int, sc: int, new_color: int) -> List[List[int]]:
        self.rows, self.cols = len(image), len(image[0])
        self.color = image[sr][sc]
        self.image = image

        if self.color == new_color:
            return image

        stack = deque()
        stack.append((sr, sc))

        while stack:
            (r, c) = stack.pop()

            image[r][c] = new_color
            stack.extend(self.getSameColorNeighbors(r, c))

        return image

    def getSameColorNeighbors(self, r, c):
        neighbors = []
        for dr, dc in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            if self.isValidCell(r + dr, c + dc) and self.image[r + dr][c + dc] == self.color:
                neighbors.append((r + dr, c + dc))

        return neighbors

    def isValidCell(self, r, c):
        return 0 <= r < self.rows and 0 <= c < self.cols


# ---------------------------------------------------
#                    Test Cases
# ---------------------------------------------------
solution = Solution()
#   [2,2,2],
#   [2,2,0],
#   [2,0,1]
print(solution.floodFill([
    [1,1,1],
    [1,1,0],
    [1,0,1]], 1, 1, 2))
