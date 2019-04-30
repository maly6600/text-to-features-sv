# class Student(object):
#     def __init__(self, name, age, gender, level, grades=None):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.level = level
#         self.grades = grades or {}
#
#     def setGrade(self, course, grade):
#         self.grades[course] = grade
#
#     def getGrade(self, course):
#         return self.grades[course]
#
#     def getGPA(self):
#         return sum(self.grades.values())/len(self.grades)
#
# # Define some students
# john = Student("John", 12, "male", 6, {"math":3.3})
# jane = Student("Jane", 12, "female", 6, {"math":3.5})
#
# # Now we can get to the grades easily
# print(john.getGPA())
# print(jane.getGPA())

class Token (object):
    def __init__(self, string, kind, length, subkind=None,  vowel=None):
        self.string = string
        self.kind = kind
        self.length = length
        self.subkind = subkind
        self.vowel = vowel

    def getString(self):
        return self.string

    def getKind(self):
        return self.kind

    def getLength(self):
        return self.length

    def getSubkind(self):
        return self.subkind

    def hasVowel(self):
        return self.vowel