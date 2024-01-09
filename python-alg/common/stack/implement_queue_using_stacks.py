class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        self.move()
        return self.stack2.pop()

    def peek(self) -> int:
        self.move()
        return self.stack2[-1]

    def empty(self) -> bool:
        return not self.stack1 and not self.stack2

    def move(self) -> None:
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())


queue = MyQueue()
queue.push(1)
queue.push(2)
queue.push(3)

print(queue.peek())
print(queue.pop())
