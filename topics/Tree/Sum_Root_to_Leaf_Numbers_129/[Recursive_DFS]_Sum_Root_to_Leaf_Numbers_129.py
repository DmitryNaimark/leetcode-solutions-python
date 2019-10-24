# https://leetcode.com/problems/sum-root-to-leaf-numbers/
# ---------------------------------------------------
from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

# Runtime Complexity: O(N)
# Space Complexity: O(max_depth), which is O(N) in worst case(skewed Tree) or O(max_depth) in case of balanced tree.
class Solution:
    def sumNumbers(self, node: TreeNode, sum=0) -> int:
        if not node:
            return 0

        sum = sum * 10 + node.val

        if not node.left and not node.right:
            return sum

        return self.sumNumbers(node.left, sum) + self.sumNumbers(node.right, sum)


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

            if arr[i] is not None:
                node.right = TreeNode(arr[i])
                q.append(node.right)
            i += 1

    return root_node


# ---------------------------------------------------
#                    Test Cases
# ---------------------------------------------------
solution = Solution()
# 25
print(solution.sumNumbers(createBinaryTreeFromArray([1, 2, 3])))
# 1026
print(solution.sumNumbers(createBinaryTreeFromArray([4, 9, 0, 5, 1])))
