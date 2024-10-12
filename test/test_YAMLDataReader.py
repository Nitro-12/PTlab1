import os
import sys
import pytest
import yaml
from YAMLDataReader import YAMLDataReader
from Types import DataType


# Путь к папке src в sys.path
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../src')
))


class TestYAMLDataReader:

    @pytest.fixture()
    def yaml_file_content(self):
        content = [
            {
                "Иванов Иван": [["математика", 90], ["физика", 85]],
            },
            {
                "Петров Петр": [["химия", 78]],
            },
        ]
        return yaml.dump(content)

    @pytest.fixture()
    def yaml_file(self, yaml_file_content, tmpdir):
        file = tmpdir.join("students.yaml")
        file.write(yaml_file_content)
        return str(file)

    def test_read_yaml(self, yaml_file):
        reader = YAMLDataReader()
        data = reader.read(yaml_file)
        expected_data = {
            "Иванов Иван": [["математика", 90], ["физика", 85]],
            "Петров Петр": [["химия", 78]],
        }
        assert data == expected_data
