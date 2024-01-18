class Stack:
    def _init_(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Stack is empty."

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Stack is empty."

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# Example usage:
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print("Stack:", stack.items)
print("Pop:", stack.pop())
print("Peek:", stack.peek())
print("Stack size:", stack.size())
