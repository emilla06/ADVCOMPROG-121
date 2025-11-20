class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return "Stack is empty!"

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        return self.items[-1] if not self.is_empty() else None

    def display(self):
        print("Stack (top → bottom):", self.items[::-1])

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.display()

print("Popped:", stack.pop())
stack.display()
