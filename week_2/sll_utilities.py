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


    def add_back(self, new_node):
        if self.head == None:
            self.head = new_node
            return self
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node
        return self
    
    def contains(self, value):
        runner = self.head
        is_found = False
        while runner.value:
            if(runner.value == value):
                is_found = True
                return is_found
            runner = runner.next
        return is_found
    
    def length(self):
        runner = self.head
        count = 0
        if runner == None:
            print("This list is empty")
            return self
        else:
            while runner is not None:
                count += 1
                runner = runner.next
        return count

    def display_values(self):
        my_list = ''
        if not self.head:
            print("This SLL is currently empty, try adding a node with add_front")
            return self
        runner = self.head
        while runner != None:
            i = runner.value 
            my_list += str(i)
            if runner.next is not None:
                my_list += ", "
            runner = runner.next
        return my_list

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

# my_sll2.display_values()
# my_sll.display_values()
print(my_sll.contains(20))
print(my_sll.length())
print(my_sll3.display_values())