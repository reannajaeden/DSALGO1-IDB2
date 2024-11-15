class LinkedStack:
    '''LIFO stack implementation using a singly linked list for storage.'''

    class _Node:
        '''Lightweight non-public class for storing a singly linked node.'''
        __slots__ = '_element', '_next'

        def __init__(self, element, next=None):
            self._element = element
            self._next = next

    def __init__(self):
        '''Create an empty stack.'''
        self._head = None
        self._size = 0

    def __len__(self):
        '''Return the number of elements in the stack.'''
        return self._size

    def is_empty(self):
        '''Return True if the stack is empty.'''
        return self._size == 0

    def push(self, e):
        '''Add an element to the top of the stack.'''
        newest = self._Node(e, self._head)
        self._head = newest
        self._size += 1

    def pop(self):
        '''Remove and return the top element of the stack.'''
        if self.is_empty():
            raise Exception("Stack is empty!")
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer

    def __str__(self):
        '''Returns a string representation of the stack with commas.'''
        elements = []
        current = self._head
        while current:
            elements.append(str(current._element))
            current = current._next
        return ", ".join(elements)