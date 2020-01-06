# https://leetcode.com/problems/sum-of-two-integers/
# ---------------------------------------------------


# Runtime Complexity: O(1), since it's we're given a 32-bit integers
# Space Complexity: O(1)
# Idea: this logic is correct for languages, which use 32-bit binary numbers (like JS), but since Python's
#     integers are infinite, negative number -4 is 11111111...100 in Python - the number of ones(in compliment of two's
#     representation is infinite), therefore we need to use mask, to work with numbers as if they are 32-bit integers.
class Solution:
    def getSum(self, a: int, b: int) -> int:
        while b != 0:
            carry = (a & b) << 1
            a = a ^ b
            b = carry

        return a


# ---------------------------------------------------
#                    Test Cases
# ---------------------------------------------------
solution = Solution()
# 3
print(solution.getSum(1, 2))
# 1
# print(solution.getSum(-2, 3))
# 0
# print(solution.getSum(-4, 4))
# DN: Negative numbers are represented as compliment of 2.
#     It's easier to see which bits are set doing (-4) & 1, (-4) & 2, (-4) & 4, (-4) & 8, etc.
#     Since it's compliment of 2, all the bits to the left of 4 are set to 1.