# -*- coding: utf-8 -*-
import sys
import os
import pytest


# Добавляем путь к папке src в sys.path
sys.path.insert(0, os.path.abspath(os.path.join
(os.path.dirname(__file__), '../src')))

# Импортируем функцию из модуля src
from main import get_path_from_arguments


@pytest.fixture()
def correct_arguments_string() -> tuple[list[str], str]:
    return ["-p", "/home/user/file.txt"], "/home/user/file.txt"


@pytest.fixture()
def noncorrect_arguments_string() -> list[str]:
    return ["/home/user/file.txt"]


def test_get_path_from_correct_arguments(
    correct_arguments_string: tuple[list[str], str]
) -> None:
    # Проверяем корректный путь
    path = get_path_from_arguments(correct_arguments_string[0])
    assert path == correct_arguments_string[1]


def test_get_path_from_noncorrect_arguments(
    noncorrect_arguments_string: list[str]
) -> None:
    # Проверяем некорректный путь и ожидаем исключение
    with pytest.raises(SystemExit) as e:
        get_path_from_arguments(noncorrect_arguments_string[0])
    assert e.type == SystemExit
