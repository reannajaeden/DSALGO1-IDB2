from LinkedStack import LinkedStack as Stack
from LinkedQueue import LinkedQueue as Queue
from PositionalList import PositionalList as PositionalList


P = PositionalList()
P.add_first(1)
P.add_first(72)
P.add_first(81)
P.add_first(25)
P.add_first(65)
P.add_first(91)
P.add_first(11)

print("Original list:", *P)

def insertion_sort(L):
    """Sort the Positional List of comparable elements into non-decreasing order."""
    if len(L) > 1:  # No need to sort if there's only one element
        marker = L.first()
        while marker != L.last():
            pivot = L.after(marker)  # Next item to place
            value = pivot.element()
            if value > marker.element():  # Pivot is already sorted
                marker = pivot  # Pivot becomes the new marker
            else:  # Must relocate pivot
                walk = marker  # Find the leftmost value greater than pivot
                while walk != L.first() and L.before(walk).element() > value:
                    walk = L.before(walk)
                L.delete(pivot)  # Remove pivot
                L.add_before(walk, value)  # Insert pivot

insertion_sort(P)

print("Ascending List:", *P)

def insertion_sort_descending(L):
    """Sort the Positional List of comparable elements into non-increasing order."""
    if len(L) > 1:
        marker = L.first()
        while marker != L.last():
            pivot = L.after(marker)
            value = pivot.element()
            if value < marker.element():
                marker = pivot
            else:
                walk = marker
                while walk != L.first() and L.before(walk).element() < value:
                    walk = L.before(walk)
                L.delete(pivot)
                L.add_before(walk, value)


insertion_sort_descending(P)

print("Descending List:", *P)
