// # Fronts

// '''Front
// Write a method to return the value (not the node) at the head of the list. If the list is empty, return null.'''

// '''Remove Front
// Write a method to remove the head node and return the new list head node. If the list is empty, return null.'''


// '''Add Front
// Write a method that accepts a value and create a new node, assign it to the list head, and return a pointer to the new head node.'''



// '''Bonus
// Add to Back
// Write a method that accepts a value and create a new node, assign it to the end of the list'''

class Node{
    constructor(val){
        this.value = val;
        this.next = null;
    }
}

class Sll{
    constructor(){
        this.head = null;
    }
    
    addFront(value){
        var newNode = new Node(value);
        newNode.next = this.head;
        this.head = newNode;
        return this.head
    }
}

var my_sll = new Sll()
console.log(my_sll.head)
// node_1 = Node(20)
// node_2 = Node(17)
// node_3 = Node(1000)

my_sll.addFront(20)
my_sll.addFront(17)
my_sll.addFront(1000)
console.log(my_sll)