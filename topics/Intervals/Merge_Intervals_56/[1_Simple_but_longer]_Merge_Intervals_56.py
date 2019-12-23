# https://leetcode.com/problems/merge-intervals/
# ---------------------------------------------------
from typing import List

# Runtime Complexity: O(N * log(N))
# Space Complexity: O(1), if we don't count the output
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) < 2:
            return intervals

        # Sort ascending (it's enough to sort only by start)
        intervals.sort(key=lambda interval: interval[0])

        merged = []

        cur_start, cur_end = intervals[0]
        for i in range(1, len(intervals)):
            if cur_end >= intervals[i][0]:
                cur_end = max(intervals[i][1], cur_end)
            else:
                merged.append([cur_start, cur_end])
                cur_start, cur_end = intervals[i]

        merged.append([cur_start, cur_end])

        return merged


# ---------------------------------------------------
#                    Test Cases
# ---------------------------------------------------
solution = Solution()
# [[1,6],[8,10],[15,18]]
print(solution.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
# [[1,5]]
print(solution.merge([[1, 4], [4, 5]]))
