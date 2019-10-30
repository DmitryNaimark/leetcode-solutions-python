# https://leetcode.com/problems/copy-list-with-random-pointer/
# ---------------------------------------------------
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

# Runtime Complexity: O(N)
# Space Complexity: O(N)
class Solution:
    def __init__(self):
        self.map_old_new = {}

    def getClonedNode(self, node):
        if node is None:
            return None

        if node in self.map_old_new:
            return self.map_old_new[node]

        new_node = Node(node.val, None, None)
        self.map_old_new[node] = new_node

        return new_node

    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None

        old_ptr = head

        new_ptr = Node(head.val, None, None)
        self.map_old_new = {head: new_ptr}

        while old_ptr:
            new_ptr.next = self.getClonedNode(old_ptr.next)
            new_ptr.random = self.getClonedNode(old_ptr.random)

            old_ptr = old_ptr.next
            new_ptr = new_ptr.next

        return self.map_old_new[head]


# ---------------------------------------------------
#                    Test Cases
# ---------------------------------------------------
# Unfortunately, since LeetCode used "Node" instead of "ListNode", I can't use my helper functions
# "createLinkedListFromArray" and "createArrayFromLinkedList", so let's just create the list of "Node"-s manually.
#
# Create node1 -> node2 -> node3 -> None list
#        r->n3    r->n1    r->n3
node1 = Node(1, None, None)
node2 = Node(2, None, None)
node3 = Node(3, None, None)
node1.next = node2
node2.next = node3
node1.random = node3
node2.random = node1
node3.random = node3

solution = Solution()
res = solution.copyRandomList(node1)
