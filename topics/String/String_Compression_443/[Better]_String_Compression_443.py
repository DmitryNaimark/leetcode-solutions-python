# https://leetcode.com/problems/string-compression/
# ---------------------------------------------------
from typing import List

# Runtime Complexity: O(N)
# Space Complexity: O(log10(max_count))
class Solution:
    def compress(self, chars: List[str]) -> int:

        left = count = 0

        for i, ch in enumerate(chars):
            count += 1

            if i + 1 == len(chars) or chars[i + 1] != ch:
                chars[left] = ch
                left += 1
                if count > 1:
                    digits = str(count)
                    for digit in digits:
                        chars[left] = digit
                        left += 1
                count = 0

        return left


# ---------------------------------------------------
#                    Test Cases
# ---------------------------------------------------
solution = Solution()
print(solution.compress(["a", "a", "b", "b", "c", "c", "c"]))
print(solution.compress(["a"]))
print(solution.compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]))
