# https://leetcode.com/problems/contains-duplicate/
# ---------------------------------------------------
from typing import List

# Runtime Complexity: O(N)
# Space Complexity: O(N)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

# ---------------------------------------------------
#                    Test Cases
# ---------------------------------------------------
solution = Solution()
# True
print(solution.containsDuplicate([1, 2, 3, 1]))
# False
print(solution.containsDuplicate([1, 2, 3, 4]))
# True
print(solution.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
