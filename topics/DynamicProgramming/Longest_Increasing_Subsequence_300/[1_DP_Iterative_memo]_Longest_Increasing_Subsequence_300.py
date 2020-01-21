# https://leetcode.com/problems/longest-increasing-subsequence/
# ---------------------------------------------------
from collections import deque
from typing import List

# Runtime Complexity: O(n^2) I think, because there are 2 branches with depth of n max.
# Space Complexity: O(n)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        q = deque()
        q.append((float('-inf'), 0, 0))

        max_subseq = 0
        memo = {}

        while q:
            num, i, subseq_len = q.popleft()

            if i >= len(nums):
                max_subseq = max(subseq_len, max_subseq)
                continue

            if subseq_len <= memo.get((num, i), -1):
                continue

            memo[(num, i)] = subseq_len

            if num < nums[i]:
                q.append((nums[i], i + 1, subseq_len + 1))
            q.append((num, i + 1, subseq_len))

        return max_subseq


# ---------------------------------------------------
#                    Test Cases
# ---------------------------------------------------
solution = Solution()
# 4
print(solution.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
