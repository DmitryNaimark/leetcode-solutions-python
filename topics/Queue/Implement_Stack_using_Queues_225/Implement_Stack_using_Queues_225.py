# https://leetcode.com/problems/implement-stack-using-queues/
# ---------------------------------------------------

from collections import deque

# Runtime Complexity:
#     Push:     O(N)
#     Pop:      O(1)
#     Top:      O(1)
#     Empty:    O(1)
# Space Complexity: O(N)
class MyStack:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.q.popleft()

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.q[0]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.q) == 0


# ---------------------------------------------------
#                    Test Cases
# ---------------------------------------------------
stack = MyStack()
stack.push(1)
stack.push(2)
print(stack.top())
print(stack.pop())
print(stack.empty())
