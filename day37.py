def func1():
  try:
    l = [1, 5, 6, 7]
    i = int(input("Enter the index: "))
    print(l[i])
    return 1
  except:
    print("Some error occurred")
    return 0

  finally:
    print("I am always executed")
  # print("I am always executed")


x = func1()
print(x)

#practiced code
def fun2():
  try:
    l=[2,4,5,6,7]
    i=int (input("enter the index:"))
    print(l[i])
    return 1
  except:
    print("Some error occured")
    return 0 
  finally:
    print("i am always executed")
y=fun2()
print(y)