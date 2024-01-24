class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.items:
            return None
        return self.items.pop(0)

    def is_empty(self):
        return not self.items

    def size(self):
        return len(self.items)

    def print_queue(self):
        print(self.items)

if __name__ == '__main__':
    queue = Queue()

    queue.enqueue(4)
    queue.enqueue(5)
    queue.enqueue(6)

    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())

    print(queue.is_empty())

