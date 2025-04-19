class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"имя: {self.name}, возраст: {self.age}")


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def display_info(self):
        super().display_info()
        print(f"ID студента: {self.student_id}")


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject
        self.students = []

    def add_student(self, student):
        if isinstance(student, Student):
            self.students.append(student)
            print(f"студент {student.name} добавлен к преподавателю {self.name}")
        else:
            print("объект не является студентом")

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)
            print(f"студент {student.name} удален из списка преподавателя {self.name}")
        else:
            print("студент не найден в списке")

    def list_students(self):
        if self.students:
            print(f"студенты, которых ведет {self.name}:")
            for student in self.students:
                student.display_info()
        else:
            print(f"у преподавателя {self.name} нет студентов")


student1 = Student("Алексей", 20, "S123")
student2 = Student("Мария", 22, "S456")
teacher = Teacher("Иван Иванович", 40, "Математика")
teacher.add_student(student1)
teacher.add_student(student2)
teacher.list_students()
teacher.remove_student(student1)
teacher.list_students()