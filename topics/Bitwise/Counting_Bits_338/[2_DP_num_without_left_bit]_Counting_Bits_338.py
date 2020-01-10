# https://leetcode.com/problems/counting-bits/
# ---------------------------------------------------
from typing import List

# Runtime Complexity: O(num)
# Space Complexity: O(1) if we don't count the res
# Idea: for 11010 check result for already calculated 1010 and add 1 (for left bit, which is 1)
class Solution:
    def countBits(self, num: int) -> List[int]:
        res = [0] * (num + 1)

        bit, i = 1, 0
        while bit <= num:
            while i < bit and i + bit <= num:
                res[i + bit] = res[i] + 1

                i += 1

            i = 0
            bit <<= 1

        return res


# ---------------------------------------------------
#                    Test Cases
# ---------------------------------------------------
solution = Solution()
# [0,1,1]
print(solution.countBits(2))
# [0,1,1,2,1,2]
print(solution.countBits(5))
