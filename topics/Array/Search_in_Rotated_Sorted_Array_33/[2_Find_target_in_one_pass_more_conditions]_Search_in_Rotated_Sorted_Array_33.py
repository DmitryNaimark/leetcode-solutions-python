# https://leetcode.com/problems/search-in-rotated-sorted-array/
# ---------------------------------------------------
from typing import List

# Runtime Complexity: O(log(N))
# Space Complexity: O(1)
# Idea: Use <= for easier binary search, check in which part is mid located(is array rotated between mid and left or right).
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        left, right = 0, len(nums) - 1

        # Invariants:
        # [-Inf, left) - doesn't contain target
        # (right, Inf] - doesn't contain target
        # [left, right] - might contain target
        while left <= right:
            mid = left + ((right - left) // 2)

            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[left]:
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1


# ---------------------------------------------------
#                    Test Cases
# ---------------------------------------------------
solution = Solution()
# 4
print(solution.search([4, 5, 6, 7, 0, 1, 2], 0))
# -1
print(solution.search([4, 5, 6, 7, 0, 1, 2], 3))
# -1
print(solution.search([], 3))
# -1
print(solution.search([1, 3], 2))
