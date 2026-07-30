def add_two_numbers() -> int:
    string:str = str(input())
    integers_list:List[int] = list()
    for i in string.split(","):
        i_int = int(i)
        integers_list.append(i_int)        
    return(integers_list[0] + integers_list[1])



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
