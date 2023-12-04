def add_more(num):
    if(num >= 9): 
        return num + 1
    
    total = num + 1
    print(total)

    return add_more(total)

add_more(0)