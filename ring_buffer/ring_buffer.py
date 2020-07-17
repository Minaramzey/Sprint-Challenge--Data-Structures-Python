class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buff = []
        self.next_item = 0

    def append(self, item):
        if len(self.buff) < self.capacity:
            self.buff.append(item)
            if self.next_item < (self.capacity - 1):
                self.next_item += 1
            else:
                self.next_item = 0
        else:
            self.buff.pop(self.next_item)
            self.buff.insert(self.next_item, item)
            if self.next_item < (self.capacity - 1):
                self.next_item +=1
            else:
                self.next_item = 0

    def get(self):
        return self.buff