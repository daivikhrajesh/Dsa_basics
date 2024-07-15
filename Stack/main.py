class Stack:
    def __init__(self):
        self.stack = []

    def push(self,item):
        self.stack.append(item)
    
    def is_empty(self):
        return len(self.stack) == 0

    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("empty list")
    
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None

    def size(self):
        return len(self.stack)
    

if __name__ == '__main__':

    stack_ = Stack()
    stack_.push(1)
    stack_.push(2)
    stack_.push(3)
    stack_.push(4)

        # Check the size of the stack
    print("Size of stack:", stack_.size())

    # Peek at the top item of the stack
    print("Top of stack:", stack_.peek())

    # Pop items from the stack
    print("Popped item:", stack_.pop())
    print("Popped item:", stack_.pop())

    # Check if the stack is empty
    print("Is stack empty?", stack_.is_empty())