class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Circular_ll:
    def __init__(self):
        self.head = None


    def insert_at_beginning(self, data):
        new_node = Node(data)  
        if not self.head:  # If the list is empty
            self.head = new_node
            new_node.next = self.head  # Circular link
        else:
            new_node.next = self.head  # Link new node to the current head
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node  # Link last node to new node
            self.head = new_node  # Make new node the new head


    def insert_at_end(self, data):
        new_node = Node(data)  # Create a new node
        if not self.head:  # If the list is empty
            self.head = new_node
            new_node.next = self.head  # Circular link
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node  # Link last node to new node
            new_node.next = self.head  # Circular link
   
    def Print_cll(self):
        if not self.head:
            return
        current = self.head
        while True:
            print(current.data, end=" ")
            current = current.next
            if current == self.head:
                break
        print()
   
    

if __name__ == '__main__':
    cll = Circular_ll()

    cll.insert_at_beginning(1)
    cll.insert_at_beginning(3)
    cll.insert_at_beginning(5)

    cll.insert_at_end(7)
    cll.insert_at_end(9)

    cll.Print_cll()