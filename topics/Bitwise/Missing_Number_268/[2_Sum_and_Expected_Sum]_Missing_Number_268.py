# https://leetcode.com/problems/missing-number/
# ---------------------------------------------------
from typing import List

# Runtime Complexity: O(N)
# Space Complexity: O(1), which might not be true, since sum can get very large and in Python numbers might occupy
#                   non-constant space, since they have infinite range.
# Idea: Compare expected sum (Gauss' formula - arithmetic progression) and nums sum.
#     There is a potential overflow issue(if it wasn't Python)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        expected_sum = n / 2 * (n + 1)
        return int(expected_sum - sum(nums))


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
