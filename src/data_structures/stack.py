class Stack:
    """
    Stack implementation using a Python list.
    Follows LIFO principle (Last In, First Out).
    """
    def __init__(self):
        self.items = [] # "items" will hold all elements of the stack

    def push(self, value):
        """ Adds an element to the top of the stack. """
        self.items.append(value)

    def pop(self):
        """ Removes and returns the top element. """
        if self.is_empty(): # calls to is_empty
            print("Stack is empty!")
            return None
        return self.items.pop()

    def peek(self):
        """ Returns the top element without removing it. """
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        """ Returns True if the stack contains no elements."""
        return len(self.items) == 0 # True if empty, False if not

    def size(self):
        """Returns the number of elements in the stack."""
        return len(self.items)