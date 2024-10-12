# -*- coding: utf-8 -*-
import yaml
from Types import DataType
from DataReader import DataReader


class YAMLDataReader(DataReader):
    def __init__(self) -> None:
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        with open(path, encoding='utf-8') as file:
            data = yaml.safe_load(file)
            for student_data in data:
                for student, grades in student_data.items():
                    # Присваиваем grades (словарь предметов и оценок) напрямую
                    self.students[student] = grades  # grades - это словарь
        return self.students
