# https://leetcode.com/problems/climbing-stairs/
# ---------------------------------------------------


# Runtime Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    memo = {}

    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        if n in self.memo:
            return self.memo[n]

        self.memo[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.memo[n]


# ---------------------------------------------------
#                    Test Cases
# ---------------------------------------------------
solution = Solution()
# 0
print(solution.climbStairs(0))
# 1
print(solution.climbStairs(1))
# 2
print(solution.climbStairs(2))
# 3
print(solution.climbStairs(3))
# 5
print(solution.climbStairs(4))
# 8
print(solution.climbStairs(5))
# 13
print(solution.climbStairs(6))