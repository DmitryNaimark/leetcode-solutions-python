# https://leetcode.com/problems/merge-intervals/
# ---------------------------------------------------
from typing import List

# Runtime Complexity: O(N * log(N))
# Space Complexity: O(1), if we don't count the output
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort ascending (it's enough to sort only by start)
        intervals.sort(key=lambda interval: interval[0])

        merged = []
        for interval in intervals:
            if len(merged) == 0 or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(interval[1], merged[-1][1])

        return merged


# ---------------------------------------------------
#                    Test Cases
# ---------------------------------------------------
solution = Solution()
# [[1,6],[8,10],[15,18]]
print(solution.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
# [[1,5]]
print(solution.merge([[1, 4], [4, 5]]))
