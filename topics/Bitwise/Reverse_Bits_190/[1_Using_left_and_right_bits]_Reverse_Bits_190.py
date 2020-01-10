# https://leetcode.com/problems/reverse-bits/
# ---------------------------------------------------


# Runtime Complexity: O(32) => O(1)
# Space Complexity: O(1)
# Idea: Go from left bit to right bit in original number, at the same time from right bit to left for result.
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        num_bit = 1 << 31
        res_bit = 1

        while num_bit > 0:
            if n & num_bit:
                res |= res_bit

            num_bit >>= 1
            res_bit <<= 1

        return res

# ---------------------------------------------------
#                    Test Cases
# ---------------------------------------------------
solution = Solution()
# 00000010100101000001111010011100 (43261596) => 00111001011110000010100101000000 (964176192)
print(solution.reverseBits(43261596))