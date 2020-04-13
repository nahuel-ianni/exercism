class School:
    def __init__(self):
        self.students = {}

    def add_student(self, name, grade):
        if self._grade_exists(grade):
            self.students[grade].append(name)
            self.students[grade].sort()
        else:
            self.students[grade] = [name]

    def roster(self):
        return [name for k, values in sorted(self.students.items()) for name in values]

    def grade(self, grade):
        return self.students[grade] if self._grade_exists(grade) else []

    def _grade_exists(self, grade):
        return grade in self.students.keys()
