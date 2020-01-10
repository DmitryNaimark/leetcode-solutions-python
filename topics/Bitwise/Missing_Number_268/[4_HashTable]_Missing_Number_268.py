# https://leetcode.com/problems/missing-number/
# ---------------------------------------------------
from typing import List

# Runtime Complexity: O(N)
# Space Complexity: O(N)
# Idea: Use set to find number which is not in the array
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_set = set(nums)

        for num in range(0, len(nums) + 1):
            if num not in nums_set:
                return num


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
