# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# ---------------------------------------------------
from typing import List

# Runtime Complexity: O(log(N))
# Space Complexity: O(1)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]:
            return nums[0]

        left, right = 0, len(nums) - 1

        # Invariants:
        # [left, right] contains min element
        # [-Inf, left) - doesn't contain min element
        # (right, Inf] - doesn't contain min element
        while left < right:
            mid = left + ((right - left) // 2)

            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1

        return nums[right]


# ---------------------------------------------------
#                    Test Cases
# ---------------------------------------------------
solution = Solution()
# 1
print(solution.findMin([3, 4, 5, 1, 2]))
# 0
print(solution.findMin([4, 5, 6, 7, 0, 1, 2]))
