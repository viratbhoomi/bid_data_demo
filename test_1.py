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

class prime_numbers():
    def __init__(self,num):
        self.num = num

    def display_3(self):
        if self.num>1:
            for i in range(2,self.num):
                if (self.num%i)==0:
                    print(self.num, " is not a prime number")
                    break
            else:
                print(self.num, " is a prime number")
        else:
            print(self.num, " is not a prime number")     

                


x = demo_class_2("Vikram",45,"Chennai","India","Single","IT",35000)
print(x.display_2())
y = prime_numbers(3)
y.display_3()
    
