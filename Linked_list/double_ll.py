class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None


class Double_LL:
    def __init__(self):
        self.head = None
        self.tail = None

    def Insert_at_begining(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head= new_node
            self.tail= new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head =  new_node

    def Insert_at_end(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head= new_node
            self.tail= new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        
    def Print_forward(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


    def Print_backward(self):
        current = self.tail
        while current:
            print(current.data, end=" ")
            current = current.prev
        print()

if __name__ == '__main__':
    dll = Double_LL()

    dll.Insert_at_begining(4)
    dll.Insert_at_end(5)
    dll.Insert_at_end(7)
    dll.Insert_at_end(11)


    dll.Print_forward()
    dll.Print_backward()





