class StudentAnalyzer:
    def __init__(self, students: dict):
        self.students = students

    def find_student(self):
        for student, grades in self.students.items():
            # Считаем количество оценок, которые равны 76
            count_grades = sum(1 for score in grades.values() if score == 76)

            # Проверяем, есть ли у студента три или более оценки 76
            if count_grades >= 3:
                return student  # Возвращаем первого подходящего студента

        return "Студентов с минимум тремя оценками >= 76 нет."
