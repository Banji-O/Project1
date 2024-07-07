# Stack Array

# There are Push operation to stack and Pop operation to fetch last element
# This is known as Last In First Out Operation (LIFO)
# Push/Pop element: O(1)
# Search element by value: O(n)
# Using list in python for stack is not recommended. It has to copy all the items in memory to a new memory if additional elementis to be added
# collections.deque is used, instead of list


# Stack Implementation

from collections import deque

stack = deque()

print(dir(stack))

stack.append("https://www.cnn.com/")
stack.append("https://www.cnn.com/world")
stack.append("https://www.cnn.com/nigeria")
stack.append("https://www.cnn.com/india")
stack.append("https://www.cnn.com/china")

print(stack)


class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

s = Stack()
s.push(5)

print(s.peek())