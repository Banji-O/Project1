class Node:
    def __init__(self, data=None, next=None):
        # Initialize a node with data and a reference to the next node
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        # Initialize the linked list with an empty head
        self.head = None

    def insert_at_beginning(self, data):
        # Create a new node and point it to the current head
        node = Node(data, self.head)
        # Update the head to the new node
        self.head = node

    def print(self):
        # Print the linked list
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        listr = ""

        while itr:
            listr += str(itr.data) + "-->"
            itr = itr.next
        print(listr)

    def insert_at_end(self, data):
        # Insert a new node at the end of the linked list
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_values(self, data_list):
        # Insert multiple values into the linked list
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        # Get the length of the linked list
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count

    def remove_at(self, index):
        # Remove a node at a specific index
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        # Insert a node at a specific index
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.insert_at_beginning(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):
        # Insert a new node after the node with the specified value
        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert, itr.next)
                itr.next = node
                return
            itr = itr.next
        raise ValueError(f"{data_after} not found in the list")

    def remove_by_value(self, data):
        # Remove the first node that contains the specified value
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                return
            itr = itr.next
        raise ValueError(f"{data} not found in the list")

if __name__ == "__main__":
    # Create a new linked list and insert initial values
    ll = LinkedList()
    ll.insert_values(["banana", "mango", "grapes", "orange"])
    ll.insert_at(0, "figs")
    # Insert a node at index 2
    ll.insert_at(2, "jack-fruit")
    ll.print()  # Print the current list

    # Insert a value after a specified value
    ll.insert_after_value("mango", "apple")
    ll.print()  # Print the list after insertion

    # Remove a node with the specified value

    ll.remove_by_value("figs")
    ll.print()  # Print the list after removal


# Doubly Linked List

class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data  # Initialize the node's data
        self.next = next  # Initialize the next pointer
        self.prev = prev  # Initialize the previous pointer

class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the list
        self.tail = None  # Initialize the tail of the list

    def insert_at_end(self, data):
        # Insert a new node at the end of the list
        if self.head is None:
            # If the list is empty, create the first node
            new_node = Node(data)
            self.head = self.tail = new_node
        else:
            # Otherwise, add the new node at the end and update pointers
            new_node = Node(data, None, self.tail)
            self.tail.next = new_node
            self.tail = new_node

    def print_forward(self):
        # Print the list in the forward direction
        if self.head is None:
            print("Doubly linked list is empty")
            return

        itr = self.head
        listr = ""
        while itr:
            listr += str(itr.data) + " <--> "
            itr = itr.next
        print(listr + "None")

    def print_backward(self):
        # Print the list in the backward direction
        if self.tail is None:
            print("Doubly linked list is empty")
            return

        itr = self.tail
        listr = ""
        while itr:
            listr += str(itr.data) + " <--> "
            itr = itr.prev
        print(listr + "None")

if __name__ == "__main__":
    # Create a new doubly linked list and insert some values
    dll = DoublyLinkedList()
    dll.insert_at_end("banana")
    dll.insert_at_end("mango")
    dll.insert_at_end("grapes")
    dll.insert_at_end("orange")

    # Print the list in forward direction
    print("Forward direction:")
    dll.print_forward()

    # Print the list in backward direction
    print("Backward direction:")
    dll.print_backward()
