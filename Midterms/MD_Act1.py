class Stack:
    def __init__(self):
        self.stack = []

    # Push Operation
    def push(self, item):
        self.stack.append(item)
        print(f"Pushed {item} to stack")

    # Pop Operation
    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.stack.pop()

    def top(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def __len__(self):
        return len(self.stack)


    def __str__(self):
        return str(self.stack)

def stack_operation():
    S = Stack()

    print("S.push(5)")
    S.push(5)
    print("S.push(3)")
    S.push(3)
    print(f"Length of Stack: {len(S)}")

    print("S.pop()")
    print(S.pop())
    print(f"Length of Stack: {len(S)}")

    print(f"S.is_empty(): {S.is_empty()}")

    print("S.pop()")
    print(S.pop())
    print(f"S.is_empty(): {S.is_empty()}")

    try:
        print("S.pop()")
        S.pop()
    except IndexError as item:
        print(f"Error: {item}")

    print("S.push(7)")
    S.push(7)

    print("S.push(9)")
    S.push(9)

    print(f"S.top(): {S.top()}")
    print("Current Stack:", str(S))

    print("S.push(4)")
    print(S.push(4))
    print(f"Length of Stack: {len(S)}")

    print(f"S.pop(): {S.pop()}")

    print("S.push(6)")
    print(S.push(6))
    print("S.push(8)")
    print(S.push(8))
    print(f"S.pop(): {S.pop()}\n")
    print("The Values returned are:", str(S))

stack_operation()

#simulation
def all_stack():
    S = Stack()
    operations = ["push(5)", "push(3)", "pop()", "push(2)", "push(8)", "pop()", "pop()",
        "push(9)", "push(1)", "pop()", "push(7)", "push(6)", "pop()", "pop()","push(4)", "pop()", "pop()"]
    returned_values = []

    for op in operations:
        if op.startswith("push"):
            value = int(op[5:-1])
            S.push(value)
            print(f"Push {value}")
        elif op == "pop()":
            if not S.is_empty():
                value = S.pop()
                returned_values.append(value)
                print(f"Pop: {value}")
            else:
                print("Pop: Stack is empty")

    print("\nPop Values returned:")
    print(returned_values)

all_stack()
