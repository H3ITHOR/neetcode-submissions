from typing import List

def read_integers() -> List[int]:
    s:str = input()
    s_split:List[str] = s.split(",")
    s_int:List[int] = list()
    for i in s_split:
        s_int.append(int(i))
    return s_int

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
