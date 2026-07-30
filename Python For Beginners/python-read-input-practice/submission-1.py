def add_two_numbers() -> int:
    # string:str = str(input())
    # integers_list:List[int] = list()
    # # for i in string.split(","):
    # #     integers_list.append(int(i))        
    # return(integers_list[0] + integers_list[1])
    # OR
    s:str = input()
    S:List[str] = s.split(",")
    return int(S[0]) + int(S[1])

# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
