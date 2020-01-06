# https://leetcode.com/problems/number-of-1-bits/
# ---------------------------------------------------


# Runtime Complexity: O(1), since 32-bit signed integers
# Space Complexity: O(1)
class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')


# ---------------------------------------------------
#                    Test Cases
# ---------------------------------------------------
solution = Solution()
# 3
print(solution.hammingWeight(11))
# 1
print(solution.hammingWeight(64))
# 5
print(solution.hammingWeight(31))
