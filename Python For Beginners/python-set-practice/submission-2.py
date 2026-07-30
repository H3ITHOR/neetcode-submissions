from typing import List

def contains_duplicate(words: List[str]) -> bool:
    # 1° way:
    # if(len(words) > len(set(words))):
    #     return True
    # return False

    # 2° way:
    # sw = sorted(words)
    # for i in range(len(sw)-1):
    #     if sw[i] == sw[i+1]:
    #         return True
    # return False

    # 3° way:
    return (len(words) > len(set(words)))


# do not modify code below this line
print(contains_duplicate(["hello", "world", "hello"]))
print(contains_duplicate(["hello", "world", "i", "am", "great"]))
print(contains_duplicate(["hello", "hello", "hello"]))
print(contains_duplicate(["Hello", "hellooo", "hello"]))
