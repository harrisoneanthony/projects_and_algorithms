class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Sll:
    def __init__(self):
        self.head = None

    def add_front(self, new_node):
        if self.head == None:
            self.head = new_node
            return self
        new_node.next = self.head
        self.head = new_node
        return self

    def display_values(self):
        if not self.head:
            print("This SLL is currently empty, try adding a node with add_front")
            return self
        runner = self.head
        while runner != None:
            print(runner.value)
            runner = runner.next
        return self

    def add_back(self, new_node):
        if self.head == None:
            self.head = new_node
            return self
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node
        return self

my_sll = Sll()
my_sll2 = Sll()
my_sll3 = Sll()

node_1 = Node(20)
node_2 = Node(17)
node_3 = Node(1000)
node_4 = Node(1)

my_sll.add_front(node_1)
my_sll.add_front(node_2)

my_sll3.add_back(node_3)
my_sll3.add_back(node_4)
# my_sll3.add_back(node_2)
# print(my_sll.head.value)

my_sll2.display_values()
my_sll.display_values()
my_sll3.display_values()