# a=4  false
# b="4"  false

# a=3  true
# b=3  true

# a=(1,2) true as it is immutable
# b=(1,2)  true

a=[1,2,43]
b=[1,2,43]

print(a is b) #exact location of object in memory
print(a==b)#value
