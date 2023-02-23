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
            return "This SLL is currently empty, try adding a node with add_front"
        runner = self.head
        while runner:
            my_list += f"{runner.value} "
            runner = runner.next
        return my_list
    
# SList: Max
# Create method max() to return list’s largest val.
    def find_max(self):
        if self.head == None:
            return "The list is empty"
        maximum = self.head
        runner = self.head
        while runner != None:
            if runner.value > maximum.value:
                maximum = runner
                runner = runner.next
            runner = runner.next
        return maximum.value

# SList: Min
# Create min(node) to return list’s smallest val.
    def find_min(self):
        if self.head == None:
            return "The list is empty"
        minimum = self.head
        runner = self.head
        while runner:
            if runner.value < minimum.value:
                minimum = runner
                runner = runner.next
            runner = runner.next
        return minimum.value

# SList: Average
# Create average() to return average val.
    def average(self):
        if self.head == None:
            return "The list is empty"
        count = 0
        total = 0
        runner = self.head
        while runner:
            count +=1
            total += runner.value
            runner = runner.next
        average = total/count
        return average

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
my_sll3.add_back(node_2)
# print(my_sll.head.value)

print(my_sll2.display_values())
print(my_sll.display_values())
print(my_sll3.contains(20))
print(my_sll3.length())
print(my_sll3.display_values())
print(my_sll3.find_max())
print(my_sll3.find_min())
print(my_sll3.average())
