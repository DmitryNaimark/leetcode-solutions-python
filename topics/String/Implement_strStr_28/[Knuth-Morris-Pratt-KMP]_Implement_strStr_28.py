# https://leetcode.com/problems/implement-strstr/
# ---------------------------------------------------


# Runtime Complexity: O(haystack + needle)
# Space Complexity: O(needle)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0

        return kmp_search(haystack, needle)


def kmp_search(haystack, needle):
    lps = create_lps_table(needle)

    i_n = 0
    i_h = 0

    while i_h < len(haystack):
        if haystack[i_h] == needle[i_n]:
            # If it's the last char
            if i_n == len(needle) - 1:
                return i_h - len(needle) + 1

            i_h += 1
            i_n += 1
        else:
            if i_n > 0:
                i_n = lps[i_n - 1]
            else:
                i_n = 0
                i_h += 1

    return -1


def create_lps_table(needle):
    n = len(needle)
    lps = [0] * n

    left = 0
    right = 1
    while right < n:
        if needle[right] == needle[left]:
            lps[right] = left + 1
            left += 1
            right += 1
        else:
            if left > 0:
                left = lps[left - 1]
            else:
                lps[right] = 0
                right += 1

    return lps


# ---------------------------------------------------
#                    Test Cases
# ---------------------------------------------------
solution = Solution()
# 2
print(solution.strStr("hello", "ll"))
# -1
print(solution.strStr("aaaaa", "bba"))
