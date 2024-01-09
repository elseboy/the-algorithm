class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        val = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(val)

    def pop(self):
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]


# Test case
min_stack = MinStack()

min_stack.push(3)
min_stack.push(5)
min_stack.push(2)
min_stack.push(8)

print("Minimum value in the stack:", min_stack.getMin())  # Output: 2
print("Top element of the stack:", min_stack.top())  # Output: 8
min_stack.pop()
print("Minimum value in the stack after pop:", min_stack.getMin())  # Output: 2
min_stack.push(1)
print("Top element of the stack after push:", min_stack.top())  # Output: 1
