# Fronts
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

    def remove_front(self):
        if self.head == None:
            return self.head
        removed_node = self.head
        self.head = removed_node.next
        removed_node.next = None
        return self.head

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
print(my_sll.head)
node_1 = Node(20)
node_2 = Node(17)
node_3 = Node(1000)

my_sll.add_front(node_1)
print(my_sll)
# my_sll.add_front(node_2)
# my_sll.add_front(node_3)
print(my_sll.head.value)

'''Front
Write a method to return the value (not the node) at the head of the list. If the list is empty, return null.'''

'''Remove Front
Write a method to remove the head node and return the new list head node. If the list is empty, return null.'''


'''Add Front
Write a method that accepts a value and create a new node, assign it to the list head, and return a pointer to the new head node.'''


'''Bonus
Add to Back
Write a method that accepts a value and create a new node, assign it to the end of the list'''