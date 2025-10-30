class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f'{self.name}正在吃饭.')

    def sleep(self):
        print(f'{self.name}正在睡觉.')


class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

    def study(self, course_name):
        print(f'{self.name}正在学习{course_name}.')


class Teacher(Person):

    def __init__(self, name, age, title):
        super().__init__(name, age)
        self.title = title

    def teach(self, course_name):
        print(f'{self.name}{self.title}正在讲授{course_name}.')