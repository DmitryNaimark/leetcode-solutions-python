# https://leetcode.com/problems/check-if-it-is-a-straight-line/
# ---------------------------------------------------
from typing import List

# Runtime Complexity: O(N)
# Space Complexity: O(1)
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        (p, q), (u, v) = coordinates[:2]

        return all(self.rectArea(x, y, p, q, u, v) == 0 for x, y in coordinates[2:])

    def rectArea(self, x1, y1, x2, y2, x3, y3):
        # Formula for Rectangle Area:
        # S = 0.5 * x1(y2 - y3) + x2(y3 - y2) + x3(y1 - y2)
        return x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)


# ---------------------------------------------------
#                    Test Cases
# ---------------------------------------------------
solution = Solution()
# True
print(solution.checkStraightLine([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]))
# False
print(solution.checkStraightLine([[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]))
