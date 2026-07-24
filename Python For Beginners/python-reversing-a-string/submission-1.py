def reverse_string(input_string: str) -> str:
    # return input_string[::-1]
    start, end, step = len(input_string)-1, 0, -1
    return input_string[start::step]

# do not modify below this line
print(reverse_string("NeetCode"))
print(reverse_string("Hello!"))
print(reverse_string("Bye Bye"))
