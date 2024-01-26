class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            print("The stack is empty")
        return self.items.pop()

    def peek(self):
        if len(self.items) == 0:
          print("The stack is empty")
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)



stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push("Krishna")
print(stack.pop())  
print(stack.peek()) 
print(stack.is_empty())  
print(stack)  

