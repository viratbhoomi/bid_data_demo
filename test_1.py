class demo_class_1():
    def __init__(self,name,age,city,country):
        self.name = name
        self.age = age
        self.city = city
        self.country = country

    def display_1(self):
        return self.name, self.age, self.city, self.country


class demo_class_2(demo_class_1):
    def __init__(self,name,age,city,country,status,employment,salary):
        super().__init__(name, age, city, country)
        self.status = status
        self.employment = employment
        self.salary = salary

    def display_2(self):
        return self.name, self.age, self.city, self.country, self.status, self.employment, self.salary


x = demo_class_2("Vikram",45,"Chennai","India","Single","IT",35000)
print(x.display_2())
    
