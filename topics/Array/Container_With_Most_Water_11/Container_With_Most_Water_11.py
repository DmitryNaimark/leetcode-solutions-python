# https://leetcode.com/problems/container-with-most-water/
# ---------------------------------------------------
from typing import List

# Runtime Complexity: O(N)
# Space Complexity: O(1)
# Idea: use two pointers.
#     Move shorter pointer toward taller one, since by moving the taller, we can't get a higher area(we're always restricted by shorter container)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0, n - 1

        max_area = 0
        while left < right:
            max_area = max(self.get_area(height, left, right), max_area)

            if height[left] < height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
            else:
                left += 1
                right -= 1

        return max_area

    def get_area(self, height, left, right):
        return (right - left) * min(height[left], height[right])


# ---------------------------------------------------
#                    Test Cases
# ---------------------------------------------------
solution = Solution()
# 49
print(solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
# 4
print(solution.maxArea([1, 2, 4, 3]))
# 24
print(solution.maxArea([1, 3, 2, 5, 25, 24, 5]))
