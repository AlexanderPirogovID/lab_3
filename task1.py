class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []

    def add_grade(self, grade):
        if 0 <= grade <= 10:
            self.grades.append(grade)
            print(f"оценка {grade} добавлена для студента {self.name}")
        else:
            print("оценка должна быть в диапазоне от 0 до 10")

    def get_average(self):
        if self.grades:
            average = sum(self.grades) / len(self.grades)
            return round(average, 2)
        else:
            return 0

    def display_info(self):
        print(f"имя студента: {self.name}")
        print(f"ID студента: {self.student_id}")
        print(f"оценки: {self.grades}")
        print(f"средний балл: {self.get_average()}")


