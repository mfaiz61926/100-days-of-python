#Strings are immutable 
#for notes just see repel or watch the video in any case.
a="!!!Harry!! !!!!! !!!!! Harry !!!!!"
print(len(a))
print(a)
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("Harry","john"))
print(a.split(" "))

blog="introduction to python CLASS"
print(blog.capitalize())

str1="welcome to the console !!!"
print(len(str1))
print(str1.center(50))
print(len(str1.center(50)))
print(a.count("Harry"))

print(str1.endswith("!!!"))
print(str1.endswith("to",4,10))

print(str1.find("the"))

str2="Hello friends"
print(str2.isalnum())
print(str2.isalpha())
print(str2.islower())
print(str2.isprintable())
print(str2.isspace())
print(str2.istitle())
print(str2.startswith("Hello"))
print(str2.swapcase())
str3="Hello friends what are you doing in your respected groups"
print(str3.title())
