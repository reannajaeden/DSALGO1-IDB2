from LinkedQueue import LinkedQueue
from LinkedDeque import LinkedDeque

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
while current != D._trailer:
    print(current._element, end=" ")
    current = current._next

print()

D.insert_last(D.delete_first())
current = D._header._next
while current != D._trailer:
    print(current._element, end=" ")
    current = current._next
print()

D.insert_last(D.delete_first())
current = D._header._next
while current != D._trailer:
    print(current._element, end=" ")
    current = current._next
print()

D.insert_last(D.delete_first())
current = D._header._next
while current != D._trailer:
    print(current._element, end=" ")
    current = current._next
print()

four = D.delete_first()
current = D._header._next
while current != D._trailer:
    print(current._element, end=" ")
    current = current._next
print()

five = D.delete_first()
current = D._header._next
while current != D._trailer:
    print(current._element, end=" ")
    current = current._next
print()

D.insert_last(five)
current = D._header._next
while current != D._trailer:
    print(current._element, end=" ")
    current = current._next
print()

D.insert_last(four)
current = D._header._next
while current != D._trailer:
    print(current._element, end=" ")
    current = current._next
print()

D.insert_last(D.delete_first())
current = D._header._next
while current != D._trailer:
    print(current._element, end=" ")
    current = current._next
print()

D.insert_last(D.delete_first())
current = D._header._next
while current != D._trailer:
    print(current._element, end=" ")
    current = current._next
print()

D.insert_last(D.delete_first())
current = D._header._next
while current != D._trailer:
    print(current._element, end=" ")
    current = current._next
