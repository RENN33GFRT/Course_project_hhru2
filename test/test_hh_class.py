import pytest
import os
import json
from src.saver_class import JSONSaver
from src.hh_class import Vacancy


@pytest.fixture
def temp_file(tmp_path):
    file = tmp_path / "test.json"
    yield file
    if os.path.exists(file):
        os.remove(file)


@pytest.fixture
def sample_vacancy():
    return Vacancy("Python", "url", 100000, 150000, "Python experience")


def test_save_and_read(temp_file, sample_vacancy):
    saver = JSONSaver({"items": [sample_vacancy.main_data()]}, str(temp_file))
    saver.save_to_file()

    data = saver.read_file()
    assert isinstance(data, dict)
    assert len(data.get("vacancies", [])) == 1


def test_add_vacancy(temp_file, sample_vacancy):
    saver = JSONSaver({"items": []}, str(temp_file))
    saver.add_vacancy(sample_vacancy.main_data())

    data = saver.read_file()
    assert len(data["vacancies"]) == 1
    assert data["vacancies"][0]["name"] == "Python"


def test_clear_file(temp_file, sample_vacancy):
    saver = JSONSaver({"items": [sample_vacancy.main_data()]}, str(temp_file))
    saver.save_to_file()
    saver.clear_file()

    data = saver.read_file()
    assert data == {"vacancies": []}


def test_invalid_vacancy(temp_file, capsys):
    saver = JSONSaver({"items": []}, str(temp_file))
    saver.add_vacancy("invalid")
    assert "можно добавлять только main_data" in capsys.readouterr().out.lower()
