import argparse
import sys
from CalcRating import CalcRating
from TextDataReader import TextDataReader
from Students_calc_var6 import StudentAnalyzer
from YAMLDataReader import YAMLDataReader


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument(
        "-p",
        dest="path",
        type=str,
        required=True,
        help="Path to datafile"
    )
    args = parser.parse_args(args)
    return args.path


def main() -> None:

    path = get_path_from_arguments(sys.argv[1:])

    reader = YAMLDataReader()
    students = reader.read(path)
    print("Студенты: ", students)
   
    analyzer = StudentAnalyzer(students)
    student = analyzer.find_student()
    print("Студент, получивший как минимум 3 оценки по 76 баллов: ", student)


if __name__ == "__main__":
    main()
