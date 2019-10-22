# https://leetcode.com/problems/implement-queue-using-stacks/
# ---------------------------------------------------
from collections import deque


# Runtime Complexity:
#     push: O(1)
#     pop: O(N)
#     peek: O(1)
#     empty: O(1)
# Space Complexity: O(N)
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = deque()
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
        temp_stack = deque()
        while self.s1:
            temp_stack.append(self.s1.pop())

        popped = temp_stack.pop()
        if temp_stack:
            self.front = temp_stack[-1]
        else:
            self.front = None

        while temp_stack:
            self.s1.append(temp_stack.pop())

        return popped

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.front

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.s1) == 0


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
