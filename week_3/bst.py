class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

class Bst:
    def __init__(self):
        self.root = None

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
            else:
                if monkey.left != None:
                    monkey = monkey.left
                else:
                    monkey.left = new_node
            return self


my_bst = Bst()

node1 = Node(45)
node2 = Node(15)
node3 = Node(88)

my_bst.add(node1)
my_bst.add(node2)
my_bst.add(node3)
print(my_bst.root.value)
print(my_bst.root.left.value)
print(my_bst.root.right.value)