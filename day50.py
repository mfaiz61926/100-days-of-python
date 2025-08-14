f=open('day50.txt','r')
i=0
while True:
    i=i+1
    line=f.readline()

    if not line:
        break

    m1=line.split(",")[0]
    m2=line.split(",")[1]
    m3=line.split(",")[2]
    print(f"Marks of student {i} in maths is: {m1}")
    print(f"Marks of student {i} in maths is: {m2}")
    print(f"Marks of student {i} in maths is: {m3}")

    #writelines write etc...