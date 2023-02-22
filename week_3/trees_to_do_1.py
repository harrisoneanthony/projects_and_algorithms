class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class Bst:
    def __init__(self):
        self.root = None


# BST: Add
# # Create an add(val) method on the BST object to add new value to the tree. This entails creating a BTNode with this value and connecting it at the appropriate place in the tree. Unless specified otherwise, BSTs can contain duplicate values.
    def add(self, new_node):
        if self.root == None:
            self.root = new_node
            return self
        monkey = self.root
        while monkey:
            if new_node.value >= monkey.value:
                if monkey.right != None:
                    monkey = monkey.right
                else:
                    monkey.right = new_node
                    return self
            else:
                if monkey.left != None:
                    monkey = monkey.left
                else:
                    monkey.left = new_node
                    return self
        return self


# BST: Contains
# # Create a contains(val) method on BST that returns whether the tree contains a given value. Take advantage of the BST structure to make this a much more rapid operation than SList.contains() would be.
    def contains(self, node_check):
        monkey = self.root
        if self.root == None:
            return False
        while monkey:
            if node_check.value == monkey.value:
                return True
            elif node_check.value > monkey.value:
                monkey = monkey.right
                if monkey == node_check:
                    return True
            else:
                monkey = monkey.left
                if monkey == node_check:
                    return True
        return False

# BST: Min
# Create a min() method on the BST class that returns the smallest value found in the BST.
    def min_value(self):
        if self.root == None:
            print("Your tree is empty")
            return self
        monkey = self.root
        minimum = self.root.value
        while monkey.left:
            if monkey.left.value < minimum:
                minimum = monkey.left.value
            monkey = monkey.left
        return minimum


# BST: Max
# Create a max() BST method that returns the largest value contained in the binary search tree.

# BONUS: BST: Size 
# Write a size() method that returns the number of nodes (values) contained in the tree.

# BONUS: BST: Is Empty
# Create an isEmpty() method to return whether the BST is empty (whether it contains no values).
my_bst = Bst()

node1 = Node(45)
node2 = Node(15)
node3 = Node(88)
node4 = Node(9)
node5 = Node(99)
node6 = Node(16)

my_bst.add(node1)
my_bst.add(node2)
my_bst.add(node3)
my_bst.add(node4)
my_bst.add(node5)
my_bst.add(node6)

# print(my_bst.root.value)
# print(my_bst.root.left.value)
# print(my_bst.root.right.value)
print(my_bst.contains(Node(45)))
print(my_bst.contains(Node(12)))
print(my_bst.contains(Node(15)))
print(my_bst.contains(Node(88)))
print(my_bst.contains(Node(9)))
print(my_bst.contains(Node(99)))
print(my_bst.contains(Node(16)))
print(my_bst.min_value())