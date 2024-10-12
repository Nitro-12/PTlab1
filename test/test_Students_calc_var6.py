import pytest

from src.Students_calc_var6 import StudentAnalyzer


class TestStudentAnalyzer:

    @pytest.fixture()
    def students_data(self):
        """Фикстура для предоставления данных студентов."""
        return {
            "Алексеев И.И.":
                {"математика": 76, "русский": 76, "физика": 76},
            "Петров П.П.":
                {"математика": 76, "русский": 76, "физика": 76, "химия": 76},
            "Сидоров С.С.":
                {"математика": 76, "русский": 75, "физика": 76},
            "Кузнецов К.К.":
                {"математика": 70, "русский": 75, "физика": 65},
        }

    def test_student_with_three_grades_equal_76(self, students_data):
        """Тестируем случай, когда у студента три оценки равные 76."""
        analyzer = StudentAnalyzer(students_data)
        result = analyzer.find_student()
        assert result in ["Алексеев И.И.", "Петров П.П."]

    def test_student_with_more_than_three_grades_equal_76(self, students_data):
        """Тестируем случай, когда у студента более трех оценок равных 76."""
        analyzer = StudentAnalyzer(students_data)
        result = analyzer.find_student()
        assert result in ["Алексеев И.И.", "Петров П.П."]

    def test_student_with_less_than_three_grades_equal_76(self, students_data):
        """Тестируем случай, когда у студента меньше трех оценок равных 76."""
        students = {
            "Сидоров С.С.": {"математика": 76, "русский": 75, "физика": 76},
        }
        analyzer = StudentAnalyzer(students)
        result = analyzer.find_student()
        assert result == "Студентов с минимум тремя оценками = 76 нет."

    def test_no_students(self):
        """Тестируем случай, когда нет студентов."""
        students = {}
        analyzer = StudentAnalyzer(students)
        result = analyzer.find_student()
        assert result == "Студентов с минимум тремя оценками = 76 нет."

    def test_multiple_students_with_no_high_grades(self):
        """Тестируем случай, когда у нескольких студентов
                    нет трех высоких оценок."""
        students = {
            "Кузнецов К.К.": {"математика": 70, "русский": 75, "физика": 65},
            "Федоров Ф.Ф.": {"математика": 72, "русский": 70, "физика": 74},
        }
        analyzer = StudentAnalyzer(students)
        result = analyzer.find_student()
        assert result == "Студентов с минимум тремя оценками = 76 нет."
