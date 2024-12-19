
#LIFO - Last In, First Out (Waiting in a line at disney land)

class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):               # adds (Enqueue) an item to the tail of the queue (index 0 of list)
        self.items.insert(0, item)      # use insert to 

    def pop(self):
        if len(self.items) == 0:        # removes (Dequeue) and returns an item from the head of the queue (last index of list)
            return None
        return self.items.pop()

    def peek(self):                     # returns an item from the head of the queue
        if len(self.items) == 0:
            return None
        return self.items[-1]

    def size(self):                     # returns the number of items in the queue
        return len(self.items)