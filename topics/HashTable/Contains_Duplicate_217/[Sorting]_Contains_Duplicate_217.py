# https://leetcode.com/problems/contains-duplicate/
# ---------------------------------------------------
from typing import List

# Runtime Complexity: O(N*log(N))
# Space Complexity: O(1)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i]:
                return True

        return False

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
