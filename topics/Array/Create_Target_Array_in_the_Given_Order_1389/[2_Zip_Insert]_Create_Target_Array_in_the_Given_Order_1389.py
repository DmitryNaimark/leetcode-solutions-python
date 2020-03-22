# https://leetcode.com/problems/create-target-array-in-the-given-order/
# ---------------------------------------------------
from typing import List

# Runtime Complexity: O(N ^ 2) in worst case, when we insert in the beginning, shifting all elements to the right.
# Space Complexity: O(N), since we're using additional N * 2 space for zipped list.
class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        res = []

        for num, ind in zip(nums, index):
            res.insert(ind, num)

        return res


# ---------------------------------------------------
#                    Test Cases
# ---------------------------------------------------
solution = Solution()
# [0,4,1,3,2]
print(solution.createTargetArray([0, 1, 2, 3, 4], [0, 1, 2, 2, 1]))
# [0,1,2,3,4]
print(solution.createTargetArray([1, 2, 3, 4, 0], [0, 1, 2, 3, 0]))
# [1]
print(solution.createTargetArray([1], [0]))
