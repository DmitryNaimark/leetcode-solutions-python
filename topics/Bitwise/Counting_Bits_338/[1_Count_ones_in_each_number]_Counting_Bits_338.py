# https://leetcode.com/problems/counting-bits/
# ---------------------------------------------------
from typing import List

# Runtime Complexity: O(num * k), where k is the avg. amount of bits in numbers.
# Space Complexity: O(1) if we don't count the res
# Idea: just count ones in each number.
class Solution:
    def countBits(self, num: int) -> List[int]:
        res = [0] * (num + 1)

        for i in range(1, num + 1):
            res[i] = self.ones_count(i)

        return res

    def ones_count(self, num: int) -> int:
        count = 0
        while num > 0:
            count += 1
            num &= (num - 1)

        return count


# ---------------------------------------------------
#                    Test Cases
# ---------------------------------------------------
solution = Solution()
# [0,1,1]
print(solution.countBits(2))
# [0,1,1,2,1,2]
print(solution.countBits(5))
