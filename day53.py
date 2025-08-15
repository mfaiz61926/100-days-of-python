#MAP
def cube(x):
    return x*x*x

print(cube(6))

l=[1,2,3,4,5,6]
newl=[]
for item in l:
    newl.append(cube(item))

print(newl)

# map datastructure
newl=list(map(cube,l))
print(newl)

# FILTER
def filter_function(a):
    return a>4
newnewl=list(filter(filter_function,l))
print(newnewl)

#REDUCE 
from functools import reduce
numbers=[1,2,3,4,5]
#cal the sum of the numbers using reduce func
sum=reduce(lambda x,y:x+y,numbers)
print(sum)