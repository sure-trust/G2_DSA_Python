class CircularQueue:
    def __init__(self, size):
        self.items = [None] * size
        self.front = 0
        self.rear = 0

    def enqueue(self, item):
        if self.is_full():
         print Exception("Queue is full")

        self.items[self.rear] = item
        self.rear = (self.rear + 1) % len(self.items)

    def dequeue(self):
        if self.is_empty():
          print Exception("Queue is empty")

        item = self.items[self.front]
        self.front = (self.front + 1) % len(self.items)
        return item

    def is_full(self):
        return self.rear == (self.front - 1) % len(self.items)

    def is_empty(self):
        return self.rear == self.front

    def size(self):
        return (self.rear - self.front) % len(self.items)

if __name__ == '__main__':
    queue = CircularQueue(5)

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    
   print(queue.is_empty())

