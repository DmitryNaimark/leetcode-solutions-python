# https://leetcode.com/problems/implement-queue-using-stacks/
# ---------------------------------------------------
from collections import deque


# Runtime Complexity:
#     push: O(1)
#     pop: O(1) amortized
#     peek: O(1)
#     empty: O(1)
# Space Complexity: O(N)
class MyQueue:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = deque()
        self.s2 = deque()
        self.front = None

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.s1.append(x)
        if len(self.s1) == 1:
            self.front = x

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if len(self.s2) > 0:
            return self.s2.pop()

        while self.s1:
            self.s2.append(self.s1.pop())

        return self.s2.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.s2:
            # peek top element
            return self.s2[-1]

        return self.front

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not (self.s1 or self.s2)


# ---------------------------------------------------
#                    Test Cases
# ---------------------------------------------------
solution = MyQueue()
solution.push(1)
solution.push(2)
# 1
print(solution.peek())
# 1 - since we pop from the front(left)
print(solution.pop())
# False
print(solution.empty())
