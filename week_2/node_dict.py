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
        return self

my_sll = Sll()
print(my_sll.head)
node_1 = Node(20)
node_2 = Node(17)
node_3 = Node(1000)

my_sll.add_front(node_1)
my_sll.add_front(node_2)
print(my_sll.head.value)
