# https://leetcode.com/problems/reverse-bits/
# ---------------------------------------------------


# Runtime Complexity: O(32) => O(1)
# Space Complexity: O(1)
# Idea: Check each of 32 bits in for loop (similar to previous).
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        # We can't use while n > 0, because we need to handle the left-most bits being zeros.
        for i in range(32):
            res <<= 1

            res |= (n & 1)

            n >>= 1

        return res

# ---------------------------------------------------
#                    Test Cases
# ---------------------------------------------------
solution = Solution()
# 00000010100101000001111010011100 (43261596) => 00111001011110000010100101000000 (964176192)
print(solution.reverseBits(43261596))