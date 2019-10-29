# https://leetcode.com/problems/flood-fill/
# ---------------------------------------------------
from collections import deque
from typing import List

# Runtime Complexity: O(N), where N is the amount of same-colored neighbors
# Space Complexity: O(N) in worst case, if same-colored neighbors are in positioned as continuous line.
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, new_color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        color = image[sr][sc]

        if color == new_color:
            return image

        def floodFillRecursively(r, c):
            if image[r][c] == color:
                image[r][c] = new_color

                if r > 0: floodFillRecursively(r - 1, c)
                if r < rows - 1: floodFillRecursively(r + 1, c)
                if c > 0: floodFillRecursively(r, c - 1)
                if c < cols - 1: floodFillRecursively(r, c + 1)

        floodFillRecursively(sr, sc)

        return image


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
