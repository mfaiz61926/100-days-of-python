class person:
    name="harry"
    occupation="software developer"
    networth=10
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a=person()
b=person()
c=person()
a.name="shubham"
a.occupation="accountant"
b.name="nitika"
b.occupation="HR"

# print(a.name,a.occupation)
a.info()
b.info()