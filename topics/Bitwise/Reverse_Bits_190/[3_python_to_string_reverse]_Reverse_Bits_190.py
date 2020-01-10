# https://leetcode.com/problems/reverse-bits/
# ---------------------------------------------------


# Runtime Complexity: O(32) => O(1)
# Space Complexity: O(32) => O(1)
# Idea: convert to binary string, reverse, convert to int.
class Solution:
    def reverseBits(self, n: int) -> int:
        # 0: to fill in all the zeros at the start
        binary_str = '{0:032b}'.format(n)
        reversed_binary_str = binary_str[::-1]
        return int(reversed_binary_str, 2)

# ---------------------------------------------------
#                    Test Cases
# ---------------------------------------------------
solution = Solution()
# 00000010100101000001111010011100 (43261596) => 00111001011110000010100101000000 (964176192)
print(solution.reverseBits(43261596))