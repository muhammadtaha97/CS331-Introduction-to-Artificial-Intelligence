
"You will have to import the Queue class to use it in your implementation"
from util import Queue

toStack = [1,2,3,4,5]

class StackTheQueue:
    "A container with a last-in-first-out (LIFO) queuing policy."
    def __init__(self):
        "Add Adequate queues!"
        self.Queue = []


    def push(self,item):
        "Push 'item' onto the stack"
        self.Queue.append(item)

    def pop(self):
        "Pop the most recently pushed item from the stack"
        _queue = self.Queue
        for _ in range(len(_queue) - 1):
            _queue.append(_queue.pop(0))
        return _queue.pop(0)


    def isEmpty(self):
        "Returns true if the queue is empty"
        return len(self.Queue) == 0

if __name__ == '__main__':

    myStack = StackTheQueue()

    #Push all values onto the stack
    for i in toStack:
        myStack.push(i)

    #Pop all the entered values...
    #This should print values in toStack in descending order: 54321!
    for i in range(0,len(toStack)):
        print myStack.pop()
