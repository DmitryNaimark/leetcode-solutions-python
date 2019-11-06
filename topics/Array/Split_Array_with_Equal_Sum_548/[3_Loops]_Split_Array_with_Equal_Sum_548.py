# https://leetcode.com/problems/split-array-with-equal-sum/
# ---------------------------------------------------
from typing import List


# Runtime Complexity: O(n^3)
# Space Complexity: O(1)
class Solution:
    def splitArray(self, nums: List[int]) -> bool:
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        for i in range(1, len(prefix_sum)):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]

        def get_sum_inclusive(i, j):
            return prefix_sum[j + 1] - prefix_sum[i]

        for i in range(1, n - 5):
            for j in range(i + 2, n - 3):
                sum1 = get_sum_inclusive(0, i - 1)
                for k in range(j + 2, n - 1):
                    sum2 = get_sum_inclusive(i + 1, j - 1)

                    if sum1 == sum2 == get_sum_inclusive(j + 1, k - 1) == get_sum_inclusive(k + 1, n - 1):
                        return True

        return False


# ---------------------------------------------------
#                    Test Cases
# ---------------------------------------------------
solution = Solution()
# True
print(solution.splitArray([1, 2, 1, 2, 1, 2, 1]))
# False
print(solution.splitArray([2, 4, 5, 7, 3, 4, 5, 6, 1, 2, 3, 4, 3, 2, 1, 5, 6, 7]))
# False
print(solution.splitArray([3, 5, 3, 5, 3, 5, 3, 5, 3, 6, 5, 7, 4, 5, 6, 5]))
# False
print(solution.splitArray(
    [6284, 2052, 4671, 7951, 8299, 4321, 9980, 9495, -8844, 9634, 7087, 2707, 1527, 9889, 4452, 7149, 2654, -2848,
     -8766, 9700, 2262, 8111, 2233, 6734, -8715, 9838, 5685, 5564, 4896, -6429, 2047, -3720, 9, 7813, 5169, 2152, -6319,
     -7131, -9838, 6080, 4319, 1789, 1717, 2991, -3474, 3536, -4327, 1484, 2782, 5384, 5063, 2888, 5344, 8280, 4758,
     3287, 5395, -5620, 9745, 2374, 2344, -5749, 7750, 5945, 4976, -5311, 9009, 9486, -970, 2191, -6896, 7781, 9284,
     3504, 5055, 266, 8206, 8196, 9346, 6964, 4582, 4298, 6918, 6448, 2149, 6542, 4093, 8479, 3564, 518, 6917, 2905,
     6444, 2592, 3644, 3626, 4906, 3394, 4351, 1281, 8009, 2874, -4299, 7068, 1575, 8846, 8418, 2212, 8674, 5150, 2864,
     8031]))
