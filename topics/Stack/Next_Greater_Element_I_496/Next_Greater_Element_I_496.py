# https://leetcode.com/problems/next-greater-element-i/
# ---------------------------------------------------
from collections import deque
from typing import List


# Runtime Complexity: O(nums2 + nums1)
# Space Complexity: O(nums2), if we don't count res
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        stack = deque()
        next_greater = {}

        for num in nums2:
            while stack and num > stack[-1]:
                next_greater[stack.pop()] = num

            stack.append(num)

        # We can explicitly set numbers, which are left in the stack to -1
        # or just handle it later.
        # while stack:
        #     next_greater[stack.pop()] = -1

        res = [0] * len(nums1)
        for i, num in enumerate(nums1):
            res[i] = next_greater.get(num, -1)

        return res


# ---------------------------------------------------
#                    Test Cases
# ---------------------------------------------------
solution = Solution()
# [-1, 3, -1]
print(solution.nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))
# [3, -1]
print(solution.nextGreaterElement([2, 4], [1, 2, 3, 4]))
