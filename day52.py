def double(x):
    return x*3

print(double(5))

#same using lambda function
double1=lambda x:x*3
print(double1(9))

#example 2 for lambda func
cube=lambda x:x*x*x
print(cube(7))

#example 3 for lambda func
avg=lambda x,y:(x+y)/2
print(avg(4,8))

#you can also pass function as an argunment als0
def appl(fx,value):
    return 6+fx(value)
print(appl(cube,4))

#same using lambda
print(appl(lambda x:x*x*x,2))