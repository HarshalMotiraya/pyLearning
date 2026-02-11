# generator function that yield even umber up to a specified limit

def even__generator(limit):
    li = []
    for i in range(2,limit + 1,2):
        # print(i)
        # return i
        li.append(i)
    return li
    

# print(even__generator(2))

print(even__generator(10))