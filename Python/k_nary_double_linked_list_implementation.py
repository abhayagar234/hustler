class TreeNode:
    def __init__(self, value):
        self.value = value  # The value or data stored in the node
        self.children = []  # List to store child nodes
        self.next_sibling = None  # Pointer to the next sibling node (next branch)
        self.prev_sibling = (
            None  # Pointer to the previous sibling node (previous branch)
        )


class KaryTree:
    def __init__(self, k):
        self.root = None  # Root of the tree (starting point)
        self.k = k  # Maximum number of children (branches) each node can have

    def add_child(self, parent, child_value):
        # Create a new child node with the given value
        new_child = TreeNode(child_value)

        # If the parent node has less than 'k' children, we can add this new child
        if len(parent.children) < self.k:
            if parent.children:
                # Set the sibling pointers for double linked-list structure
                last_child = parent.children[-1]
                last_child.next_sibling = new_child
                new_child.prev_sibling = last_child

            # Add the new child to the parent's list of children
            parent.children.append(new_child)
        else:
            print(f"Cannot add more than {self.k} children to a single node")

    def traverse_tree(self, node):
        if node is None:
            return

        # Print the value of the current node
        print(node.value)

        # Recursively traverse each child
        for child in node.children:
            self.traverse_tree(child)

        # Example: To demonstrate double linked-list traversal, let's also print sibling nodes
        print(f"Siblings of {node.value}: ", end="")
        sibling = node.next_sibling
        while sibling:
            print(sibling.value, end=" -> ")
            sibling = sibling.next_sibling
        print("None")  # End of siblings


# Example of using the k-nary tree with double linked-list

# Create a k-nary tree where each node can have up to 3 children
tree = KaryTree(3)

# Create the root of the tree
tree.root = TreeNode("Root")

# Add children to the root node
tree.add_child(tree.root, "A")
tree.add_child(tree.root, "B")
tree.add_child(tree.root, "C")

# Add children to node "A"
tree.add_child(tree.root.children[0], "A1")
tree.add_child(tree.root.children[0], "A2")

# Add children to node "B"
tree.add_child(tree.root.children[1], "B1")
tree.add_child(tree.root.children[1], "B2")
tree.add_child(tree.root.children[1], "B3")

# Traverse the tree starting from the root
tree.traverse_tree(tree.root)
