# Variant 2
# Linear singly linked list with references to head and tail


class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class LinearSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # Print List
    def __str__(self):
        if self.head is not None:
            current = self.head
            result = '[' + str(current.value)
            while current.next is not None:
                current = current.next
                result += ' ' + str(current.value)
            return str(result) + ']'
        return '[]'

    # Returns length of List
    def __len__(self):
        return int(self.length)

    # Adds value to the end of List
    def add(self, x=None):
        if self.head is None:
            self.head = Node(x)
            self.tail = self.head
        elif self.head == self.tail:
            self.tail = Node(x)
            self.head.next = self.tail
        else:
            self.tail.next = Node(x)
            self.tail = self.tail.next
        self.length += 1

    # Adds value to the front of List
    def add_to_front(self, x=None):
        if self.head is None:
            self.head = Node(x)
            self.tail = self.head
        else:
            self.head = Node(x, self.head)
        self.length += 1

    # Remove an element from the end
    def remove_end(self):
        if self.tail is None:
            print("List is empty!")
        elif self.length == 1:
            self.tail = None
            self.head = None
            self.length -= 1
        else:
            self.length -= 1
            old = self.head
            current = self.head
            while current is not self.tail:
                old = current
                current = current.next
            self.tail = old
            self.tail.next = None

    # Remove an element from the front
    def remove_front(self):
        if self.tail is None:
            print("List is empty!")
        elif self.length == 1:
            self.tail = None
            self.head = None
            self.length -= 1
        else:
            self.length -= 1
            self.head = self.head.next

    # Returns element by index
    def get_element_at(self, x):
        int(x)
        if (x > self.length - 1) or (x < 0):
            print('Element at ' + str(x) + ' not found!')
            return
        else:
            current = self.head
            for i in range(1, x + 1):
                current = current.next
            print('Element at ' + str(x) + ' = '+str(current.value))
            return current.value

    # Search element for a value
    def find(self, x):
        if self.length == 0:
            print('Element not found!')
            return
        current = self.head
        for i in range(self.length):
            if current.value == x:
                print('Element ' + str(x) + ' was found! Index = ' + str(i))
                return
            current = current.next
        print('Element not found!')

    # Search all elements for a value
    def find_all(self, x):
        if self.length == 0:
            print('Element not found!')
            return
        current = self.head
        success=False
        for i in range(self.length):
            if current.value == x:
                success = True
                print('Element ' + str(x) + ' was found! Index = ' + str(i))
            current = current.next
        if not success:
            print('Element not found!')
