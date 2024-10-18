from ArrayStack import ArrayStack as Stack

def is_matched(expression):
    matching_brackets = {')': '(', '}': '{', ']': '['}
    stack = []

    for char in expression:
        if char in matching_brackets.values():
            stack.append(char)
        elif char in matching_brackets.keys():
            if not stack or stack[-1] != matching_brackets[char]:  #
                return "the symbols are not balanced"
            stack.pop()

    return "the symbols are balanced" if len(stack) == 0 else "the symbols are not balanced"

expression = input("Enter an expression to check for balanced symbols: ")

print(is_matched(expression))

def reverse_file(myfile):
    stack = Stack()

    with open(myfile, 'r') as file:
        for line in file:
            stack.push(line.rstrip('\n'))

    with open(myfile, 'w') as file:
        while not stack.is_empty():
            file.write(stack.pop() + '\n')

myfile = 'myfile.txt'
reverse_file(myfile)
print("File lines reversed!")