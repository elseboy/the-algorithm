from collections import deque


class MyStack:

    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x: int) -> None:
        while self.queue1:
            self.queue2.append(self.queue1.popleft())
        self.queue1.append(x)
        while self.queue2:
            self.queue1.append(self.queue2.popleft())

    def pop(self) -> int:
        return self.queue1.popleft()

    def top(self) -> int:
        return self.queue1[0]

    def empty(self) -> bool:
        return not self.queue1


stack = MyStack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.top())  # Output: 2
print(stack.pop())  # Output: 2
print(stack.empty())  # Output: False
