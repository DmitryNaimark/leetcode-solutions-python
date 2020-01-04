# https://leetcode.com/problems/search-in-rotated-sorted-array/
# ---------------------------------------------------
from typing import List

# Runtime Complexity: O(log(N))
# Space Complexity: O(1)
# Idea: find min index, then find target in the left or right subarray.
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        # Find min
        # Invariants:
        # [-Inf, left] - ascending
        # (left, right) - to be inspected
        # [right, Inf] - ascending

        if nums[0] < nums[-1]:
            i_min = 0
        else:
            left, right = 0, len(nums) - 1

            while right - left > 1:
                mid = left + ((right - left) // 2)

                if nums[mid] > nums[0]:
                    left = mid
                else:
                    right = mid

            i_min = right

        if nums[i_min] <= target <= nums[-1]:
            return self.binary_search(nums, i_min, len(nums) - 1, target)
        else:
            return self.binary_search(nums, 0, i_min, target)

    def binary_search(self, nums, left, right, target):
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right

        # Invariants:
        # [-Inf, left] - not a target
        # [right, Inf] - not a target
        # (left, right) - to be inspected
        while right - left > 1:
            mid = left + ((right - left) // 2)

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid
            else:
                right = mid

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
