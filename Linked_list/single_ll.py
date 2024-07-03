# Single_Linked_list

class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

class Single_ll:

    def __init__(self):
        self.head = None

    def Insert_at_beginning(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def Insert_at_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        

    def Print_ll(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()



if __name__ == '__main__':
    sll = Single_ll()

    sll.Insert_at_beginning(3)
    sll.Insert_at_end(7)
    sll.Insert_at_end(9)

    print('Single_Linked_list')
    sll.Print_ll()