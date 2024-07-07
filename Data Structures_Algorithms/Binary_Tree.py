
# All the elements of binary tree must be unique
# Value to the left of a node should by lower while, value to the right should be higher

class BinarySearchTreeNode:
    def __init__(self, data):
        # Initialize node with data and left/right child pointers
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        # Ignore if the data already exists in the tree
        if data == self.data:
            return

        # Traverse left subtree if data is less than current node's data
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        # Traverse right subtree if data is greater than current node's data
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def search(self, val):
        # Base case: value found
        if self.data == val:
            return True

        # Search left subtree if value is less than current node's data
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        # Search right subtree if value is greater than current node's data
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def in_order_traversal(self):
        elements = []
        # Traverse left subtree
        if self.left:
            elements += self.left.in_order_traversal()

        # Append current node's data
        elements.append(self.data)

        # Traverse right subtree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def find_max(self):
        # If there is no right child, return the current node's data
        if self.right is None:
            return self.data
        # Recursively find the maximum value in the right subtree
        return self.right.find_max()

    def find_min(self):
        # If there is no left child, return the current node's data
        if self.left is None:
            return self.data
        # Recursively find the minimum value in the left subtree
        return self.left.find_min()

    def delete(self, val):
        # Traverse left subtree if value is less than current node's data
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        # Traverse right subtree if value is greater than current node's data
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            # Node to be deleted found
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            # Find the maximum value in the left subtree
            max_val = self.left.find_max()
            # Replace current node's data with the maximum value from the left subtree
            self.data = max_val
            # Delete the node with the maximum value from the left subtree
            self.left = self.left.delete(max_val)

        return self

# Build a binary search tree from a list of elements
def build_tree(elements):
    print(f"Building tree with these elements: {elements}")
    # Create the root node with the first element
    root = BinarySearchTreeNode(elements[0])

    # Add each remaining element to the tree
    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == "__main__":
    # Test cases for deleting nodes from the tree
    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    # Delete node with value 20
    numbers_tree.delete(20)
    print(f"After deleting 20: {numbers_tree.in_order_traversal()}")

    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    # Delete node with value 9
    numbers_tree.delete(9)
    print(f"After deleting 9: {numbers_tree.in_order_traversal()}")

    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    # Delete node with value 17
    numbers_tree.delete(17)
    print(f"After deleting 17: {numbers_tree.in_order_traversal()}")
