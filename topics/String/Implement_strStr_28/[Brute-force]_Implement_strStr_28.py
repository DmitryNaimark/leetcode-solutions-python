# https://leetcode.com/problems/implement-strstr/
# ---------------------------------------------------


# Runtime Complexity: O(haystack * needle)
# Space Complexity: O(1)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):

            is_same = True
            for j in range(len(needle)):
                if needle[j] != haystack[i + j]:
                    is_same = False
                    break

            if is_same:
                return i

        return -1


# ---------------------------------------------------
#                    Test Cases
# ---------------------------------------------------
solution = Solution()
# 2
print(solution.strStr("hello", "ll"))
# -1
print(solution.strStr("aaaaa", "bba"))
