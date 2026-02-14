
global x
x= 12
def f1():
    x = 44
    def f2():
        print(x)
    return f2
myResult = f1()
myResult()


def chaiCoder (num):
    def actual(x):
        return x ** num 
    return actual 

def chaiCoder ():
    def actual(x):
        return x ** 2 
    return actual 

#factory function / closer

f = chaiCoder(2)
g = chaiCoder(3)

print(f(3))



print(g(3))
