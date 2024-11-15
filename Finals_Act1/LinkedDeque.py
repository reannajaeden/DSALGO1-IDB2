from DoublyLinkedBase import _DoublyLinkedBase
class LinkedDeque:
    '''Double-ended queue implementation using a doubly linked list.'''

    class _Node:
        '''Lightweight non-public class for storing a doubly linked node.'''
        __slots__ = '_element', '_prev', '_next'

        def __init__(self, element, prev, next):
            self._element = element  # user's element
            self._prev = prev  # previous node reference
            self._next = next  # next node reference

    def __init__(self):
        '''Create an empty deque.'''
        self._header = self._Node(None, None, None)  # sentinel node at the front
        self._trailer = self._Node(None, self._header, None)  # sentinel node at the back
        self._header._next = self._trailer  # header points to trailer
        self._size = 0  # number of elements in the deque

    def __len__(self):
        '''Return the number of elements in the deque.'''
        return self._size

    def is_empty(self):
        '''Return True if the deque is empty.'''
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        '''Add element e between two existing nodes and return the new node.'''
        newest = self._Node(e, predecessor, successor)  # create a new node
        predecessor._next = newest  # update predecessor's next link
        successor._prev = newest  # update successor's prev link
        self._size += 1
        return newest

    def insert_first(self, e):
        '''Insert an element at the front of the deque.'''
        self._insert_between(e, self._header, self._header._next)

    def insert_last(self, e):
        '''Insert an element at the back of the deque.'''
        self._insert_between(e, self._trailer._prev, self._trailer)

    def delete_first(self):
        '''Remove and return the element from the front of the deque.'''
        if self.is_empty():
            raise Exception('Deque is empty')
        return self._delete_node(self._header._next)

    def delete_last(self):
        '''Remove and return the element from the back of the deque.'''
        if self.is_empty():
            raise Exception('Deque is empty')
        return self._delete_node(self._trailer._prev)

    def _delete_node(self, node):
        '''Remove a non-sentinel node from the deque and return its element.'''
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor  # bypass the node
        successor._prev = predecessor
        self._size -= 1
        element = node._element  # record the element to return
        node._prev = node._next = node._element = None  # deprecate the node
        return element  # return the element from the deleted node

    def first(self):
        '''Return but do not remove the element at the front of the deque.'''
        if self.is_empty():
            raise Exception('Deque is empty')
        return self._header._next._element

    def last(self):
        '''Return but do not remove the element at the back of the deque.'''
        if self.is_empty():
            raise Exception('Deque is empty')
        return self._trailer._prev._element
