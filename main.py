#4-m
class Teacher:
    def __init__(self, name, age):
        self.name = name
        self.__age = age
        
    @property
    def age(self):
        return self.__age
    
    
    @age.setter
    def age(self, yangi):
        self.__age = yangi
        
    
t1 = Teacher("John", 22)
print(t1.age)

res = t1.age
print(res)

t1.age = 500
print(t1.age)
