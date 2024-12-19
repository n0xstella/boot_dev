
#FIFO - First In, First Out (Plate Stacking)

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):           # Places a new item on top of the stack
        self.items.append(item)

    def pop(self):                  # Places a new item on top of the stack
        if len(self.items) == 0:
            return None
        return self.items.pop()

    def peek(self):                 # Returns the top item from the stack without modifying the stack. (return None if empty)
        if len(self.items) == 0:
            return None
        return self.items[len(self.items) - 1]
    
    def size(self):                 # Returns the number of items in the stack
        return len(self.items)