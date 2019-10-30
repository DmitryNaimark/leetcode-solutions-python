# https://leetcode.com/problems/copy-list-with-random-pointer/
# ---------------------------------------------------
from collections import defaultdict

class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

# Runtime Complexity: O(N)
# Space Complexity: O(N)
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        map_old_new = defaultdict(lambda: Node(None, None, None))
        map_old_new[None] = None

        node = head
        while node:
            map_old_new[node].val = node.val
            map_old_new[node].next = map_old_new[node.next]
            map_old_new[node].random = map_old_new[node.random]
            node = node.next

        return map_old_new.get(head)


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
