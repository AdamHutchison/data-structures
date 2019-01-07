class Queue:
    def __init__(self):
        self.items = []

    def queue(self, item):
        self.items.insert(0, item)
    
    def dequeue(self):
        if self.items:
            return self.items.pop()

    def peek(self):
        if self.items:
            return self.items[-1]
    
    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0