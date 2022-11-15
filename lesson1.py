# Полиморфизм

# from random import randint
# class Triangle:
#     def __init__(self, count):
#         self.names_values = {f"side_{i}": randint(1,20) for i in range(count)}
#         self_square = 0
#
#     def get_attrs(self):
#         print(self.__dict__)
#
#     def get_list_attrs(self):
#         lists = list(self.__dict__.items())
#         print(lists)
#
#     def distract_square(self):
#         square = 1/2 * self.names_values["side_0"] * self.names_values["side_1"]
#         self.square = square
#         print(self.square)
#
# class Rectangle:
#     def __init__(self, a: int, b: int) -> None:
#         self.side_a = a
#         self.side_b = b
#         self.square = 0
#
#     def get_attrs(self):
#         print(self.__dict__)
#
#     def get_list_attrs(self):
#         lists = list(self.__dict__.items())
#         print(lists)
#
#     def distract_square(self):
#         self.square = self.side_a * self.side_b
#         print(self.square)
#
# triangle1 = Triangle(2)
# triangle2 = Triangle(2)
# rectangle1 = Rectangle(12, 6)
# rectangle2 = Rectangle(16, 4)
#
# lists = [triangle2,  rectangle1, triangle1, rectangle2]
# for i in lists:
#     i.distract_square()
#     i.get_attrs()
#     i.get_list_attrs()
# # triangle1.distract_square()
# # triangle2.distract_square()
# # triangle1.get_attrs()
# # triangle2.get_attrs()


#class Student

# class Student:
#     def __init__(self, fullname, course):
#         self.fullname = fullname
#         self.course = course
#         self.subjects = {}
#         self.total = 0
#
#     def set_subjects(self, subjects: dict) -> None:
#         self.subjects = subjects
#
#     def get_total(self):
#         self.total = sum(self.subjects.values()) / len(self.subjects)
#
#     def save_total_in_file(self):
#         with open(f"{self.fullname}.txt", "a") as f:
#             f.write(f"{self.fullname} - {self.course} - {self.total}\n")
#             for key, value in self.subjects.items():
#                 f.write(f"{key} - {value}\n")
#         self.total = 0
#         self.subjects = {}
#
#     def set_course(self):
#         self.course +=1
#
# subjects = {
#     "algebra": 56,
#     "python": 76,
# }
# subjects2 = {
#     "algebra": 56,
#     "python": 76,
#     "java": 100
# }
# nazgul = Student("Tab Naz", 2)
# nazgul.set_subjects(subjects)
# nazgul.get_total()
# nazgul.save_total_in_file()
# nazgul.set_course()
# nazgul.set_subjects(subjects2)
# nazgul.get_total()
# nazgul.save_total_in_file()

class Table:
    def __init__(self, material, color, nojki) -> None:
        self.material = material
        self.color = color
        self.nojki = nojki

trinojka = Table('wood', 'grey', 3)