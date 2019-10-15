# https://leetcode.com/problems/two-sum/
# ---------------------------------------------------
from typing import List


# Runtime Complexity: O(N)
# Space Complexity: O()
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_pos = {}
        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder in num_pos:
                return [num_pos[remainder], i]

            num_pos[nums[i]] = i


# ---------------------------------------------------
#                    Test Cases
# ---------------------------------------------------
solution = Solution()
# [0, 1]
print(solution.twoSum([2, 7, 11, 15], 9))
# [2, 5]
print(solution.twoSum([4, 8, 15, 16, 23, 42], 57))
