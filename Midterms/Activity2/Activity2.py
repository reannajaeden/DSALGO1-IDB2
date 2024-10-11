#Activity2_Sanglay
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, e):
        self.items.append(e)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Cannot dequeue from an empty queue.")
        return self.items.pop(0)

    def first(self):
        if self.is_empty():
            raise IndexError("Cannot retrieve the first element from an empty queue.")
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return f"Queue: {self.items}"
#Simulation 1
kyu = Queue()

kyu.enqueue(5)
kyu.enqueue(3)
print("Dequeued: " , kyu.dequeue())
kyu.enqueue(2)
print("Queue length: ", len(kyu))
print("Dequeued: " , kyu.dequeue())
print("Is queue empty? " ,kyu.is_empty())
print("Dequeued: " , kyu.dequeue())
print("Is queue empty? " ,kyu.is_empty())
kyu.enqueue(7)
kyu.enqueue(9)
print("First element: ",kyu.first())
kyu.enqueue(4)
print("Queue length: ", len(kyu))
print("Dequeued: " , kyu.dequeue())
print(kyu)

#Simulation 2
kyu = Queue()

kyu.enqueue(5)
kyu.enqueue(3)
print("Dequeued: " , kyu.dequeue())
kyu.enqueue(2)
kyu.enqueue(8)
print("Dequeued: " , kyu.dequeue())
print("Dequeued: " , kyu.dequeue())
kyu.enqueue(9)
kyu.enqueue(1)
print("Dequeued: " , kyu.dequeue())
kyu.enqueue(7)
kyu.enqueue(6)
print("Dequeued: " , kyu.dequeue())
print("Dequeued: " , kyu.dequeue())
kyu.enqueue(4)
print("Dequeued: " , kyu.dequeue())
print("Dequeued: " , kyu.dequeue())
print(kyu)

