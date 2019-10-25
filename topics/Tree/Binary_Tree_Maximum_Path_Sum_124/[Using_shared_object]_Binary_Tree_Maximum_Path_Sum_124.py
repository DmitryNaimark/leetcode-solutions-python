# https://leetcode.com/problems/binary-tree-maximum-path-sum/
# ---------------------------------------------------
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


# Runtime Complexity: O(N)
# Space Complexity: O(tree_height), which is O(N) in worst case of skewed tree and O(log(N)) in case of balanced tree.
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        shared_obj = {'max_sum': -2 ** 63}

        self.max_path_sum_recursively(root, shared_obj)
        return shared_obj['max_sum']

    def max_path_sum_recursively(self, node: TreeNode, shared_obj) -> int:
        if not node:
            return 0

        left_sum = max(self.max_path_sum_recursively(node.left, shared_obj), 0)
        right_sum = max(self.max_path_sum_recursively(node.right, shared_obj), 0)

        shared_obj['max_sum'] = max(left_sum + node.val + right_sum, shared_obj['max_sum'])

        return max(left_sum, right_sum) + node.val


# ---------------------------------------------------
#                Uses DN functions:
# ---------------------------------------------------
from collections import deque

def createBinaryTreeFromArray(arr):
    if arr is None or len(arr) == 0:
        return None

    root_node = TreeNode(arr[0])
    q = deque()
    q.append(root_node)

    i = 1
    while q and i < len(arr):
        node = q.popleft()

        if node:
            if arr[i] is not None:
                node.left = TreeNode(arr[i])
                q.append(node.left)
            i += 1

            if i < len(arr) and arr[i] is not None:
                node.right = TreeNode(arr[i])
                q.append(node.right)
            i += 1

    return root_node

# ---------------------------------------------------
#                    Test Cases
# ---------------------------------------------------
solution = Solution()
# 6
print(solution.maxPathSum(createBinaryTreeFromArray([1, 2, 3])))
# 42
print(solution.maxPathSum(createBinaryTreeFromArray([-10, 9, 20, None, None, 15, 7])))
# -3
print(solution.maxPathSum(createBinaryTreeFromArray([-3])))
# 2
print(solution.maxPathSum(createBinaryTreeFromArray([2, -1])))
# 4
print(solution.maxPathSum(createBinaryTreeFromArray([1, -2, 3])))
# 16
print(solution.maxPathSum(createBinaryTreeFromArray([9, 6, -3, None, None, -6, 2, None, None, 2, None, -6, -6, -6])))
