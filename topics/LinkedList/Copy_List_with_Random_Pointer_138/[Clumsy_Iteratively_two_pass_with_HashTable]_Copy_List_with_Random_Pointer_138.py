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
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None

        new_head = Node(head.val, None, None)
        new_tail = new_head

        map_old_new = {head: new_head}

        cur = head
        while cur.next:
            new_tail.next = Node(cur.next.val, None, None)
            new_tail = new_tail.next

            cur = cur.next
            map_old_new[cur] = new_tail

        cur_old, cur_new = head, new_head
        while cur_new:
            cur_new.random = map_old_new.get(cur_old.random, None)
            cur_new = cur_new.next
            cur_old = cur_old.next

        return new_head


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
