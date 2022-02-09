class queue:
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.items.insert(0, item)
    def dequeue(self):
        # stack = lifo
        #queue = fifo
        if self.items:
            self.items.pop()
        return None
    def peek(self):
        if self.items:
            self.items[-1]
        return None
    def size(self):
        return len(self.items)
    def is_size(self):
        return self.items == []
class SLLNode:  # NODE = data[1].address of next node
    def __init__(self, data):
        self.data = data
        self.next = None  #[Data, empty(no address assigned)]
    def __repr__(self):
        return "SLLNode object: data={}".format(self.data)
    def get_data(self): #return the self.data attribute
        return self.data
    def set_data(self, new_data):
        self.data = new_data
    def get_next(self):
        return self.next
    def set_next(self, new_next):
        self.next = new_next
