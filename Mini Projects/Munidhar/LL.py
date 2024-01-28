class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert(self, data, position):
        if position < 0:
            print("Invalid position")
            return

        if position == 0:
            self.prepend(data)
            return

        new_node = Node(data)
        current = self.head
        prev = None
        count = 0

        while current and count < position:
            prev = current
            current = current.next
            count += 1

        if count == position:
            prev.next = new_node
            new_node.next = current
        else:
            print("Position out of range")

    def delete(self, data):
        if not self.head:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        prev = None
        while current and current.data != data:
            prev = current
            current = current.next

        if current:
            prev.next = current.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

linked_list = LinkedList()

linked_list.append(1)
linked_list.append(2)
linked_list.append(4)

print("Initial Linked List:")
linked_list.display()

linked_list.prepend(0)
print("After prepend a new node (0):")
linked_list.display()

linked_list.insert(3, 4)
print("After insert a new node (3) at position 4:")
linked_list.display()

linked_list.delete(2)
print("After delete an existing node (2):")
linked_list.display()

