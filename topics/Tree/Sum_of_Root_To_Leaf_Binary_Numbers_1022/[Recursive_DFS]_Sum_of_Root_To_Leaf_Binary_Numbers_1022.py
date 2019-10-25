# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/
# ---------------------------------------------------
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


# Runtime Complexity: O(N)
# Space Complexity: O(max_depth), which is O(N) in worst case(skewed Tree) or O(max_depth) in case of balanced tree.
class Solution:
    def sumRootToLeaf(self, node: TreeNode, sum: int = 0) -> int:
        if not node:
            return 0

        sum = sum * 2 + node.val
        if not node.left and not node.right:
            return sum

        return self.sumRootToLeaf(node.left, sum) + self.sumRootToLeaf(node.right, sum)


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
print(solution.sumRootToLeaf(createBinaryTreeFromArray([1, 0, 1, 0, 1, 0, 1])))
