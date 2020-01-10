# https://leetcode.com/problems/missing-number/
# ---------------------------------------------------
from typing import List

# Runtime Complexity: O(N * log(N))
# Space Complexity: O(1)
# Idea: Sort, then find number, where i != nums[i]
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] > mid:
                right = mid - 1
            else:
                left = mid + 1

        return left


# ---------------------------------------------------
#                    Test Cases
# ---------------------------------------------------
solution = Solution()
# 2
print(solution.missingNumber([3, 0, 1]))
# 8
print(solution.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
# 1
print(solution.missingNumber([0]))
