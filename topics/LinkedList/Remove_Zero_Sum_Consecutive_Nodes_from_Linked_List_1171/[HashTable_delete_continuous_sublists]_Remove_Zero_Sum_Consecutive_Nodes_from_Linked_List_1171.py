# https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/
# ---------------------------------------------------
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


# Runtime Complexity: O(N)
# Space Complexity: O(N) in worst case
class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        dummy_head = ListNode(None)
        dummy_head.next = head

        sum_node = {0: dummy_head}
        cur_sum = 0

        while head:
            cur_sum += head.val

            if cur_sum in sum_node:
                # Remove from pos till cur
                prev_node = sum_node[cur_sum]

                while prev_node.next != head.next:
                    # We can use cur_sum without creating temp_sum, since cur_sum will become the same after
                    # we delete several elements, which sum to 0.
                    cur_sum += prev_node.next.val

                    # Do not remove prefix sum created by the last element, it should stay.
                    if prev_node.next != head:
                        del sum_node[cur_sum]

                    prev_node.next = prev_node.next.next

                head = prev_node.next

            else:
                sum_node[cur_sum] = head
                head = head.next

        return dummy_head.next


# ---------------------------------------------------
#                Uses DN functions:
# ---------------------------------------------------
def createLinkedListFromArray(arr):
    if len(arr) == 0:
        return None

    head = ListNode(arr[0])
    cur = head

    for i in range(1, len(arr)):
        cur.next = ListNode(arr[i])
        cur = cur.next

    return head


def createArrayFromLinkedList(head):
    res = []

    while head != None:
        res.append(head.val)
        head = head.next

    return res


# ---------------------------------------------------
#                    Test Cases
# ---------------------------------------------------
solution = Solution()
print(createArrayFromLinkedList(solution.removeZeroSumSublists(createLinkedListFromArray([1, 2, -3, 3, 1]))))
print(createArrayFromLinkedList(solution.removeZeroSumSublists(createLinkedListFromArray([1, 2, 3, -3, 4]))))
print(createArrayFromLinkedList(solution.removeZeroSumSublists(createLinkedListFromArray([1, 2, 3, -3, -2]))))
print(createArrayFromLinkedList(solution.removeZeroSumSublists(createLinkedListFromArray([2, -2, 1]))))
print(createArrayFromLinkedList(solution.removeZeroSumSublists(createLinkedListFromArray([0, 0, 0]))))
