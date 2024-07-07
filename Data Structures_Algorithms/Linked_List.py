# Linked List
# Linked list references the location address of item in the next item while doubly linked list references addresses of previous and next items
# Insertion is easier and no need to pre-allocate space

class Node:
    def __init__(self, data=None, next=None):
        # Initialize the node with data and a reference to the next node
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

if __name__ == "__main__":
    # Create a new linked list
    ll = LinkedList()
    # Insert values into the linked list
    ll.insert_values(["banana", "mango", "grapes", "orange"])
    # Print the linked list
    ll.print()
    # Print the length of the linked list
    print(f"Length: {ll.get_length()}")
    # Insert a node at the beginning
    ll.insert_at(0, "figs")
    # Insert a node at index 2
    ll.insert_at(2, "jackfruit")
    # Print the linked list again
    ll.print()

