def summ_all(*args):
    print(args)
    for i in args:
        print(i * 2)
    return sum(args)   #default parameter and we can pass many more value is there
  
print(summ_all(1,2,3))
# print(summ_all(1,2,3,4,5))
# print(summ_all(1,2,3,4,5,6,7,8))

