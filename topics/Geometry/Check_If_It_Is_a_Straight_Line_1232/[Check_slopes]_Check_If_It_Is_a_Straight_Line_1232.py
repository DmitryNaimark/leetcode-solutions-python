# https://leetcode.com/problems/check-if-it-is-a-straight-line/
# ---------------------------------------------------
from typing import List

# Runtime Complexity: O(N)
# Space Complexity: O(1)
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        [p, q] = coordinates[0]
        [u, v] = coordinates[1]

        for [x, y] in coordinates[2:]:
            # Checking slope, "fractions form":
            # if (x - p) / (y - q) != (x - u) / (y - v)

            # Transform division form to Multiplication form: x/y == a/b  => x * b == a * y
            if (x - p) * (y - v) != (x - u) * (y - q):
                return False

        return True


# ---------------------------------------------------
#                    Test Cases
# ---------------------------------------------------
solution = Solution()
# True
print(solution.checkStraightLine([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]))
# False
print(solution.checkStraightLine([[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]))
