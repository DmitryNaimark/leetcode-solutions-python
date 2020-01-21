# https://leetcode.com/problems/climbing-stairs/
# ---------------------------------------------------


# Runtime Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        prev_prev = 1
        prev = 2
        cur = 0
        for i in range(3, n + 1):
            cur = prev_prev + prev
            prev_prev, prev = prev, cur

        return cur


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