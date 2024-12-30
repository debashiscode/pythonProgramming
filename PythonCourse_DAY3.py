# Stack examples in python

stack = []
#
stack.append(1)
stack.append(2)
stack.append(3)

print("Stack after pushes:", stack[0])
# Pop elements from the stack
print("Popped element:", stack.pop())
print("Stack after pop:", stack)
#picking an element
#print("peek an element from stack", stack.peek())  this does not have the peek operation defined.


#Stack examples

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

# Push operation on stack
    def push(self, item):
        self.items.append(item)
# defining pop operation on stack
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Stack is empty")

# peek operation
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Stack is empty")

# display all items
    def display(self):
        if not self.is_empty():
            return self.items
        else:
            print("Stack is empty")

# creating a stack
stk = Stack()


#push value in stack

stk.push(1)
stk.push(2)
stk.push(3)

print("stack after push operation::", stk.display())

print("peek operation ::", stk.peek())

print("stack after peek operation::", stk.display())

print("pop operation ::", stk.pop())

print("stack after pop operation ::", stk.display())


#Example1
"""
The end of a stack, traditionally known as the position where 
PUSH and POP operations performed, is known as:


1. FIFO
2. LIFO
3. FRONT
4. TOP

"""
#ans 4

"""
The five items P,Q,R,S and T are pushed in a stack, one after the other starting from P.
The stack is popped four times and each element is inserted in a queue.
Then two elements are deleted from the queue and pushed back on the stack.
now one item is popped from the stack. The popped item is:  

1. P
2. R
3. Q
4. S


"""

#ans S


"""
Which of the following applications may use a stack?

(a) Parenthesis balancing program

(b) Process scheduling operating system

(c) Conversion of infix arithmetic expression to postfix form

(a) and (b)
(b) and (c)
(a) and (c)
(a), (b) and (c)


"""



#Answer: Option 3 : (a) and (c)