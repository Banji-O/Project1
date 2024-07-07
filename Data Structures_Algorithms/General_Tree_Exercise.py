class TreeNode:
    def __init__(self, name, position):
        # Initialize the node with a name and a position, and an empty list of children
        self.name = name
        self.position = position
        self.children = []

    def add_child(self, child_node):
        # Add a child node to the current node's list of children
        self.children.append(child_node)

    def print_tree(self, detail='both', level=0):
        # Print the tree structure starting from this node
        # detail: controls what to print (name, position, or both)
        # level: current depth level in the tree (for printing indentation)
        prefix = (" " * level * 3) + '|__'  # Create prefix for current level
        if detail == 'name':
            print(f"{prefix}{self.name}")  # Print name only
        elif detail == 'position':
            print(f"{prefix}{self.position}")  # Print position only
        else:
            print(f"{prefix}{self.name} ({self.position})")  # Print both name and position
        for child in self.children:
            child.print_tree(detail, level + 1)  # Recursively print each child node


def build_tree():
    # Build the tree structure according to the provided hierarchy

    # Level 0
    ceo = TreeNode('Nilupul', 'CEO')  # Create the CEO node

    # Level 1
    cto = TreeNode('Chinway', 'CTO')  # Create the CTO node
    hr_head = TreeNode('Gels', 'HR Head')  # Create the HR Head node

    ceo.add_child(cto)  # Add CTO as a child of CEO
    ceo.add_child(hr_head)  # Add HR Head as a child of CEO

    # Level 2 under CTO
    infra_head = TreeNode('Vishwa', 'Infrastructure Head')  # Create Infrastructure Head node
    app_head = TreeNode('Aamir', 'Application Head')  # Create Application Head node

    cto.add_child(infra_head)  # Add Infrastructure Head as a child of CTO
    cto.add_child(app_head)  # Add Application Head as a child of CTO

    # Level 3 under Infrastructure Head
    cloud_manager = TreeNode('Dhaval', 'Cloud Manager')  # Create Cloud Manager node
    app_manager = TreeNode('Abhijit', 'App Manager')  # Create App Manager node

    infra_head.add_child(cloud_manager)  # Add Cloud Manager as a child of Infrastructure Head
    infra_head.add_child(app_manager)  # Add App Manager as a child of Infrastructure Head

    # Level 2 under HR Head
    recruitment_manager = TreeNode('Peter', 'Recruitment Manager')  # Create Recruitment Manager node
    policy_manager = TreeNode('Waqas', 'Policy Manager')  # Create Policy Manager node

    hr_head.add_child(recruitment_manager)  # Add Recruitment Manager as a child of HR Head
    hr_head.add_child(policy_manager)  # Add Policy Manager as a child of HR Head

    return ceo  # Return the root of the tree


if __name__ == '__main__':
    root = build_tree()  # Build the tree and get the root node

    print("Name Tree:")
    root.print_tree(detail='name')  # Print the tree showing only names
    print("\nPosition Tree:")
    root.print_tree(detail='position')  # Print the tree showing only positions
    print("\nName and Position Tree:")
    root.print_tree(detail='both')  # Print the tree showing both names and positions



# Second Exercise

class TreeNode:
    def __init__(self, name, level):
        # Initialize a tree node with a name and level
        self.name = name
        self.level = level
        self.children = []  # Initialize an empty list for child nodes

    def add_child(self, child):
        # Add a child node to the current node
        self.children.append(child)

    def print_tree(self, level):
        # Print the tree structure up to the specified level
        if self.level <= level:
            # Print the current node with indentation based on its level
            print('   ' * self.level + '|__' + self.name)
            # Recursively print each child node
            for child in self.children:
                child.print_tree(level)


def build_tree():
    # Create the root node
    root = TreeNode("Global", 0)

    # Create nodes for India and its states and cities
    india = TreeNode("India", 1)
    gujarat = TreeNode("Gujarat", 2)
    karnataka = TreeNode("Karnataka", 2)
    # Add cities to Gujarat
    gujarat.add_child(TreeNode("Ahmedabad", 3))
    gujarat.add_child(TreeNode("Baroda", 3))
    # Add cities to Karnataka
    karnataka.add_child(TreeNode("Bangluru", 3))
    karnataka.add_child(TreeNode("Mysore", 3))
    # Add states to India
    india.add_child(gujarat)
    india.add_child(karnataka)

    # Create nodes for USA and its states and cities
    usa = TreeNode("USA", 1)
    new_jersey = TreeNode("New Jersey", 2)
    california = TreeNode("California", 2)
    # Add cities to New Jersey
    new_jersey.add_child(TreeNode("Princeton", 3))
    new_jersey.add_child(TreeNode("Trenton", 3))
    # Add cities to California
    california.add_child(TreeNode("San Francisco", 3))
    california.add_child(TreeNode("Mountain View", 3))
    # Add states to USA
    usa.add_child(new_jersey)
    usa.add_child(california)

    # Add countries to the root node
    root.add_child(india)
    root.add_child(usa)

    return root  # Return the root node


if __name__ == "__main__":
    # Build the tree structure
    root_node = build_tree()
    # Print the tree structure up to level 1
    print("\n")
    root_node.print_tree(1)
    print("\n")
    # Print the tree structure up to level 2
    root_node.print_tree(2)
    print("\n")
    # Print the tree structure up to level 3
    root_node.print_tree(3)
