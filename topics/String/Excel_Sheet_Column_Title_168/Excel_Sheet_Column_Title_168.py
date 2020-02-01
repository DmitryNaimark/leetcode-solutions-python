# https://leetcode.com/problems/excel-sheet-column-title/
# ---------------------------------------------------


# Runtime Complexity: O(log26(n)) => O(log(n))
# Space Complexity: O(log26(n)) => O(log(n)), if we take into account res, otherwise it's O(1).
class Solution:
    def convertToTitle(self, n: int) -> str:
        res = ''

        while n > 0:
            # Because Radix starts from 1 to 26.
            # In contrast to decimal Radix (which is from 0 to 9)
            n -= 1

            ch_code = n % 26
            n = (n - ch_code) // 26

            res = chr(ord('A') + ch_code) + res

        return res


# ---------------------------------------------------
#                    Test Cases
# ---------------------------------------------------
solution = Solution()
# 'A'
print(solution.convertToTitle(1))
# 'B'
print(solution.convertToTitle(2))
# 'Z'
print(solution.convertToTitle(26))
# 'AB'
print(solution.convertToTitle(28))
# 'ZY'
print(solution.convertToTitle(701))
# 'BMG'
print(solution.convertToTitle(1697))
