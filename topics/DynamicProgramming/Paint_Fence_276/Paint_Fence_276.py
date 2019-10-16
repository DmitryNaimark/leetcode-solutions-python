# https://leetcode.com/problems/paint-fence/
# ---------------------------------------------------


# Runtime Complexity: O(N)
# Space Complexity: O(1)
class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return k

        same_color = k
        diff_color = k * (k - 1)

        for i in range(2, n):
            # Amount of ways to paint next fence the same color is the same as diff_color for the previous fence.
            tmp = diff_color
            diff_color = (diff_color + same_color) * (k - 1)
            same_color = tmp

        return same_color + diff_color


# ---------------------------------------------------
#                    Test Cases
# ---------------------------------------------------
solution = Solution()
print(solution.numWays(3, 2))
