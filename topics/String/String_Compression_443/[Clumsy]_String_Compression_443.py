# https://leetcode.com/problems/string-compression/
# ---------------------------------------------------
from typing import List

# Runtime Complexity: O(N)
# Space Complexity: O(log10(max_count))
class Solution:
    def compress(self, chars: List[str]) -> int:

        left = count = 0
        n = len(chars)

        for i in range(len(chars) + 1):
            if i > 0 and (i == n or chars[i] != chars[i - 1]):
                if count > 1:
                    chars[left] = chars[i - 1]
                    num_chars = list(str(count))

                    left += 1
                    for ch in num_chars:
                        chars[left] = ch
                        left += 1

                    count = 1
                else:
                    chars[left] = chars[i - 1]
                    left += 1
            else:
                count += 1

        return left


# ---------------------------------------------------
#                    Test Cases
# ---------------------------------------------------
solution = Solution()
print(solution.compress(["a", "a", "b", "b", "c", "c", "c"]))
print(solution.compress(["a"]))
print(solution.compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]))
