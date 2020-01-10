# https://leetcode.com/problems/counting-bits/
# ---------------------------------------------------
from typing import List

# Runtime Complexity: O(num)
# Space Complexity: O(1) if we don't count the res
# Idea: for 11010 check result for already calculated 11 (we removed right-most 1) and add 1
class Solution:
    def countBits(self, num: int) -> List[int]:
        res = [0] * (num + 1)

        for i in range(1, num + 1):
            res[i] = res[i & (i - 1)] + 1

        return res


# ---------------------------------------------------
#                    Test Cases
# ---------------------------------------------------
solution = Solution()
# [0,1,1]
print(solution.countBits(2))
# [0,1,1,2,1,2]
print(solution.countBits(5))
