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

        stack = deque()
        stack.append((sr, sc))

        while stack:
            (r, c) = stack.pop()

            image[r][c] = new_color

            for dr, dc in ((-1, 0), (0, 1), (1, 0), (0, -1)):

                if 0 <= r + dr < rows and 0 <= c + dc < cols and image[r + dr][c + dc] == color:
                    stack.append((r + dr, c + dc))

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
