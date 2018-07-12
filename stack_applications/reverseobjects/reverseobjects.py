from stack import Stack

def reverseObjects(sequence):
    """Returns the contents of sequence reversed in a list."""
    reversed_list = []
    stack = Stack()

    # Do something with stack and sequence
    # ...
    # ...
    # ...
    # Return the sequence reversed

    for i in sequence:
        stack.push(i)

    while not stack.is_empty():
        reversed_list.append(stack.top())
        stack.pop()

    return reversed_list

