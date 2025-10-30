class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    @staticmethod
    def study(self, course_name):
        print(f'student name is {course_name}')

    def play(self):
        print(f'play name is {self.name} ,age is {self.age}')

stu1 = Student('wuquan',35)
print(stu1.play())
print(stu1.study(stu1,'ff'))