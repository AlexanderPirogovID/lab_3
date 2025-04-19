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

    def __str__(self):
        return f"Студент: {self.name}, ID: {self.student_id}, Оценки: {self.grades}"

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.student_id == other.student_id
        return False

    def __len__(self):
        return len(self.grades)



if __name__ == "__main__":
    student1 = Student("Алексей", "S123")
    student2 = Student("Мария", "S456")
    student3 = Student("Алексей", "S123")
    student1.add_grade(8)
    student1.add_grade(9)

    print(student1) #__str__


    print(student1 == student2)  # False
    print(student1 == student3)  # True

    print(f"Количество оценок у {student1.name}: {len(student1)}") #__len__