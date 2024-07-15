from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self,item):
        self.queue.append(item)

    def dequeue(self):

        if self.is_empty():
            raise IndexError('dequeue from empty queue')
        return self.queue.popleft()
    
    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)
    
    def front(self):

        if self.is_empty():
            raise IndexError("front from empty queue")
        return self.queue[0]
    
    def last(self):
        if self.is_empty():
            raise IndexError("front from empty queue")
        return self.queue[len(self.queue)-1]
        
    
if __name__ == '__main__':
    q= Queue()

    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)

    print("Queue size:", q.size())  # Output: Queue size: 3
    print("Front element:", q.front())  # Output: Front element: 1
    
    print("Dequeue:", q.dequeue())  # Output: Dequeue: 1
    print("Queue size after dequeue:", q.size())  # Output: Queue size after dequeue: 2
    
    print("Is queue empty?", q.is_empty()) 

    print("last item", q.last())