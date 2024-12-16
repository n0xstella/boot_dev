class LLQueue:
    def remove_from_head(self):
        if self.head is None:
            return None
        temp = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return temp

    def add_to_tail(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.tail.next = node
        self.tail = node

    def __init__(self):
        self.tail = None
        self.head = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.val)
        return " <- ".join(nodes)


class Node:
    def __init__(self, val):            # constructor: __init__(val) -> sets self.val to the given value, and initializes self.next to None
        self.val = val
        self.next = None

    def set_next(self, node):           # node.set_next(node) -> sets self.next to the given node
        self.next = node
        
    def __repr__(self):
        return self.val