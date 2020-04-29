# Default dict removes the issue of inserting keys for the first time vs appending items
# as well as returning an empty list (by initializing it with a list argument)
# for a key that doesn't exist
from collections import defaultdict


class School:
    def __init__(self):
        self.students = defaultdict(list)

    def add_student(self, name, grade):
        self.students[grade].append(name)
        self.students[grade].sort()

    def roster(self):
        return [name for k, values in sorted(self.students.items()) for name in values]

    def grade(self, grade):
        return self.students[grade]
