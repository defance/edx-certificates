import csv


class Student:

    def __init__(self, name="", student_id="", grade=""):
        self.name = name
        self.id = student_id
        if grade == '100%':
            self.grade = '1'
        else:
            self.grade = '0.' + grade.replace('%', '')

    @property
    def printed_name(self):
        splitted = self.name.split(" ")[1::-1]
        return " ".join(splitted)


def get_student_list(filename):
    """
    Get list[Student].

    Format:
    "id","Lastname Firstname Middlename"

    Returns list.
    """
    result = []
    with open(filename, 'r') as source:
        student_reader = csv.reader(source)
        for student in student_reader:
            result += [Student(student[1], student[0], student[2])]
    return result
