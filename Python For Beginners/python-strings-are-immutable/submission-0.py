def remove_fourth_character(word: str) -> str:
    p1: str = word[:3]
    p2: str = word[4:]
    return p1 + p2


# do not modify below this line
print(remove_fourth_character("NeetCode"))
print(remove_fourth_character("Hello"))
