
from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()  # Initialize the container as a deque

    def push(self, val):
        self.container.append(val)  # Add an element to the top of the stack

    def pop(self):
        return self.container.pop()  # Remove and return the top element of the stack

    def pick(self):
        return self.container[-1]  # Return the top element of the stack without removing it

    def is_empty(self):
        return len(self.container) == 0  # Check if the stack is empty

    def size(self):
        return len(self.container)  # Return the size of the stack

    def reverse_string(self, string):
        # Push each character of the string onto the stack
        for char in string:
            self.push(char)

        reversed_string = ""
        # Pop each character from the stack to form the reversed string
        while not self.is_empty():
            reversed_string += self.pop()

        return reversed_string

if __name__ == "__main__":
    stack = Stack()
    original_string = "we will conquer COVID-19"
    reversed_string = stack.reverse_string(original_string)
    print(f"Original string: {original_string}")
    print(f"Reversed string: {reversed_string}")


# Second Exercise

from collections import deque


class Stack:
    def __init__(self):
        self.container = deque()  # Initialize the container as a deque

    def push(self, val):
        self.container.append(val)  # Add an element to the top of the stack

    def pop(self):
        return self.container.pop()  # Remove and return the top element of the stack

    def pick(self):
        return self.container[-1]  # Return the top element of the stack without removing it

    def is_empty(self):
        return len(self.container) == 0  # Check if the stack is empty

    def size(self):
        return len(self.container)  # Return the size of the stack


def is_balanced(expression):
    stack = Stack()
    # Dictionary to hold matching pairs
    matching_pairs = {')': '(', '}': '{', ']': '['}
    # Set to hold opening brackets
    opening_brackets = set(matching_pairs.values())

    for char in expression:
        if char in opening_brackets:
            stack.push(char)  # Push opening brackets onto the stack
        elif char in matching_pairs:
            if stack.is_empty() or stack.pop() != matching_pairs[char]:
                return False  # Mismatched or unbalanced closing bracket

    return stack.is_empty()  # True if no unmatched opening brackets


# Test cases
print(is_balanced("((a+b))"))  # True
print(is_balanced("))((a+b)("))  # False
print(is_balanced("((a+b))"))  # True
print(is_balanced("))"))  # False
print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))  # True
