# Circular Queue Program
class CircularQueue:
    def __init__(self, size):
        self.max = size
        self.queueArray = [0] * size
        self.front = -1
        self.rear = -1


# Writing enqueue operation
    def enqueue(self, item):
        if self.front == 0 and self.rear == self.max - 1:
            print("Queue is full")
        if self.front == -1 and self.rear == -1:
            self.front = 0
            self.rear = 0
        else:

            if self.rear == self.max -1 and self.front !=0:
               self.rear = 0
            else:
               self.rear = self.rear + 1
        self.queueArray[self.rear] = item

#Delete an item from queue
    def dequeue(self):
        if self.front == -1:
            print("queue is empty")

        item = self.queueArray[self.front]
        if self.front == self.rear:
            self.front = 0
            self.rear = 0
        elif self.front == self.max -1:
            self.front = 0
        else:
            self.front = self.front + 1
        return item

    def peek(self):
        if not self.isEmpty():
            return self.queueArray[self.front]
        else:
            print("Queue is empty. No peek value.")
            return -1  # Assuming -1 represents an empty value

    def isEmpty(self):
        return self.front == -1 and self.rear == -1




# Double ended-queue
class DoubleEndedQueue:
    def __init__(self, size):
        self.max = size
        self.queueArray = [0] * size
        self.front = -1
        self.rear = -1


# Writing item from front in queue operation
    def enqueue_front(self, item):
        if (self.front == 0 and self.rear == self.max - 1) or (self.front == self.rear + 1):
            print("Queue is full")
        if self.front == -1:
            self.front = 0
            self.rear = 0
        else:
            if self.front == 0:
               self.front = self.max - 1
            else:
               self.front = self.front - 1
        self.queueArray[self.front] = item

# Writing item from front in queue operation
    def enqueue_back(self, item):
        if (self.front == 0 and self.rear == self.max - 1) or (self.front == self.rear + 1):
                print("Queue is full")
        if self.front == -1:
            self.front = 0
            self.rear = 0
        else:
            if self.rear == self.max - 1:
                self.rear = 0
            else:
                self.rear = self.rear + 1
        self.queueArray[self.rear] = item



#Delete an item from front in queue
    def dequeue_front(self):
        if self.front == -1:
            print("queue is empty")

        item = self.queueArray[self.front]
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        elif self.front == self.max -1:
            self.front = 0
        else:
            self.front = self.front + 1
        return item

# Delete an item from queue
    def dequeue_back(self):
        if self.front == -1:
            print("queue is empty")
        item = self.queueArray[self.rear]
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        elif self.rear == 0:
                self.rear = self.max - 1
        else:
            self.rear = self.rear - 1
        return item


    def peek(self):
        if not self.isEmpty():
            return self.queueArray[self.front]
        else:
            print("Queue is empty. No peek value.")
            return -1  # Assuming -1 represents an empty value

    def isEmpty(self):
        return self.front == -1 and self.rear == -1




# Hash table
class HashTable:
    def __init__(self):
        self.divisor = 97  #prime number


    def __division__(self, key):
        return key % self.divisor



if __name__ == "__main__":
    circularQueue = CircularQueue(5)

    circularQueue.enqueue(1)
    circularQueue.enqueue(2)
    circularQueue.enqueue(3)

    # Should print 1
    print("Peek:", circularQueue.peek())

    # Should print 1
    print("Dequeue:", circularQueue.dequeue())

    # Should print 2
    print("Peek after dequeue:", circularQueue.peek())


    # output restricted double ended queue
    deq = DoubleEndedQueue(5)

    deq.enqueue_front(1)
    deq.enqueue_back(2)
    deq.enqueue_back(3)

    print("print double ended peek :", deq.peek())

    deq.dequeue_front()

    print("print double ended peek :",deq.peek())


    #input restricted double ended queue
    ir_deq = DoubleEndedQueue(5)

    ir_deq.enqueue_back(1)
    ir_deq.enqueue_back(2)
    ir_deq.enqueue_back(3)

    print("print input restricted double ended peek :", deq.peek())
    ir_deq.dequeue_front()
    print("print input restricted should print 2 double ended peek :", deq.peek())
    ir_deq.dequeue_back()
    print("print input restricted should print 2 double ended peek :", deq.peek())


    # hash table divsion example
    # calculate the hash values of keys 1234 and 5462.
    hd = HashTable()
    print("hash value of 1234",hd.__division__(1234))
    print("hash value of 5462", hd.__division__(5462))



"""
Given a hash table of size 1000, map the key 12345 to an appropriate location
in the hash table.
Solution We will use A = 0.618033, m = 1000, and k = 12345
h(12345) = Î 1000 (12345 ¥ 0.618033 mod 1) ˚
h(12345) = Î 1000 (7629.617385 mod 1) ˚
h(12345) = Î 1000 (0.617385) ˚
h(12345) = Î 617.385 ˚
h(12345) = 617


"""


"""
Calculate the hash value for keys 1234 and 5642 using the mid-square method.
The hash table has 100 memory locations.

Solution Note that the hash table has 100 memory locations whose indices vary from 0 to 99.
This means that only two digits are needed to map the key to a location in the hash table, so r = 2.
When k = 1234, k2 = 1522756, h (1234) = 27
When k = 5642, k2 = 31832164, h (5642) = 21
Observe that the 3rd and 4th digits starting from the right are chosen
"""