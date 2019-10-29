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
        dummy = ListNode(0)
        dummy.next = head

        seen = {0: dummy}

        prefix_sum = 0
        while head:
            prefix_sum += head.val
            seen[prefix_sum] = head
            head = head.next

        head = dummy
        prefix_sum = 0
        while head:
            prefix_sum += head.val
            if prefix_sum in seen:
                head.next = seen[prefix_sum].next

            head = head.next

        return dummy.next



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
