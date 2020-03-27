from enum import Enum, unique


@unique
class Plants(Enum):
    C = "Clover"
    G = "Grass"
    R = "Radishes"
    V = "Violets"


class Garden:
    def __init__(self, diagram, students=None):
        self.diagram = diagram.split("\n")
        self.students = sorted(students) if students else [
            "Alice", "Bob", "Charlie", "David", "Eve", "Fred",
            "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"
        ]

    def plants(self, student):
        if student not in self.students:
            raise ValueError(f"Student {student} couldn't be found.")

        # Nested for loops
        plants = []
        index = self.students.index(student) * 2

        for keys in self.diagram:
            for cup in range(index, index + 2):
                key = keys[cup]
                plants.append(Plants[key].value)

        return plants

        # Nested list comprehension
        # index = self.students.index(student) * 2
        # return [Plants[keys[cup]].value for keys in self.diagram for cup in range(index, index + 2)]
