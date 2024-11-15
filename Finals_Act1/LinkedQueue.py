class LinkedQueue:
    '''FIFO queue implementation using a singly linked list for storage.'''

    # ---------------- nested _Node class ----------------
    class _Node:
        '''Lightweight non-public class for storing a singly linked node.'''
        __slots__ = '_element', '_next'  # streamline memory usage

        def __init__(self, element, next):
            self._element = element
            self._next = next

    # --------------- queue methods ----------------
    def __init__(self):
        '''Create an empty queue'''
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        '''Return the number of elements in the queue'''
        return self._size

    def is_empty(self):
        '''Return true if the queue is empty.'''
        return self._size == 0

    def first(self):
        '''Return but do not remove the element at the front of the queue.'''
        if self.is_empty():
            raise Exception('Queue is empty')
        return self._head._element  # front aligned with the head of the list

    def dequeue(self):
        '''Remove and return the first element of the queue (FIFO).'''
        '''Raise empty exception if the queue is empty.'''
        if self.is_empty():
            raise Exception('Queue is empty')

        answer = self._head._element
        self._head = self._head._next  # move the head pointer to the next node
        self._size -= 1

        if self.is_empty():  # special case: if the queue becomes empty
            self._tail = None  # removed head had been the tail

        return answer

    def enqueue(self, e):
        '''Add an element to the back of the queue.'''
        newest = self._Node(e, None)  # node will be the new tail node
        if self.is_empty():
            self._head = newest  # special case: queue was empty
        else:
            self._tail._next = newest  # link the old tail to the new node
        self._tail = newest  # update reference to the tail node
        self._size += 1
