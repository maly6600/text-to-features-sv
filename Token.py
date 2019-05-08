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
    def __init__(self, string, kind, length, subkind=None,  vowel=None, counted=None, lemma=None):
        self.string = string
        self.kind = kind
        self.length = length
        self.subkind = subkind
        self.vowel = vowel
        self.counted = counted
        self.lemma = lemma

    def getString(self):
        return self.string

    def getLemma(self):
        return self.lemma

    def getKind(self):
        return self.kind

    def getLength(self):
        return self.length

    def getSubkind(self):
        return self.subkind

    def hasVowel(self):
        return self.vowel

    def hasBeenCounted(self):
        return self.counted

    def setCounted(self, value):
        self.counted = value

    def setString(self, new_string):
        self.string = new_string

    def setLemma(self, new_lemma):
        self.lemma = new_lemma