from LinkedDeque import LinkedDeque  # Import LinkedDeque
from LinkedStack import LinkedStack  # Import LinkedStack

D = LinkedDeque()
D.insert_last(1)
D.insert_last(2)
D.insert_last(3)
D.insert_last(4)
D.insert_last(5)
D.insert_last(6)
D.insert_last(7)
D.insert_last(8)

current = D._header._next
print("Initial deque:")
while current != D._trailer:
    print(current._element, end=" ")
    current = current._next
print()

S = LinkedStack()

D.insert_last(D.delete_first())
D.insert_last(D.delete_first())
D.insert_last(D.delete_first())
S.push(D.delete_first())
D.insert_last(D.delete_first())
D.insert_last(S.pop())
D.insert_last(D.delete_first())
D.insert_last(D.delete_first())
D.insert_last(D.delete_first())

current = D._header._next
print("Reordered deque:")
while current != D._trailer:
    print(current._element, end=" ")
    current = current._next
