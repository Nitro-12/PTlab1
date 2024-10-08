# -*- coding: utf-8 -*-
import os
import sys
import pytest

from Types import DataType
from CalcRating import CalcRating


# Путь к папке src в sys.path
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../src')
))

RatingsType = dict[str, float]


class TestCalcRating:

    @pytest.fixture()
    def input_data(self) -> tuple[DataType, RatingsType]:
        data: DataType = {
            "Абрамов Петр Сергеевич": [
                ("математика", 80),
                ("русский язык", 76),
                ("программирование", 100),
            ],
            "Петров Игорь Владимирович": [
                ("математика", 61),
                ("русский язык", 80),
                ("программирование", 78),
                ("литература", 97),
            ],
        }
        rating_scores: RatingsType = {
            "Абрамов Петр Сергеевич": 85.3333,
            "Петров Игорь Владимирович": 79.0000,
        }
        return data, rating_scores

    def test_init_calc_rating(
        self, input_data: tuple[DataType, RatingsType]
    ) -> None:
        calc_rating = CalcRating(input_data[0])
        assert input_data[0] == calc_rating.data

    def test_calc(
        self, input_data: tuple[DataType, RatingsType]
    ) -> None:
        rating = CalcRating(input_data[0]).calc()
        for student in rating.keys():
            rating_score = rating[student]
            expected_score = input_data[1][student]
            assert pytest.approx(rating_score, abs=0.001) == expected_score
