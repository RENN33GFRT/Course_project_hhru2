import pytest
from src.hh_class import Vacancy


@pytest.fixture
def sample_vacancies():
    """Фикстура с тестовыми вакансиями"""
    return [
        Vacancy("Python Developer", "https://hh.ru/vacancy/1", 100000, 150000, "Python experience"),
        Vacancy("Java Developer", "https://hh.ru/vacancy/2", 120000, 180000, "Java experience"),
        Vacancy("Junior Python", "https://hh.ru/vacancy/3", 80000, 120000, "Basic Python")
    ]


def test_vacancy_comparison(sample_vacancies):
    """Тестирование операторов сравнения"""
    python, java, junior = sample_vacancies

    # Тесты на сравнение
    assert junior < python < java
    assert java > python > junior
    assert junior <= python <= java
    assert java >= python >= junior

    # Тесты на равенство
    python_copy = Vacancy("Python Copy", "https://hh.ru/vacancy/1c", 100000, 155000, "Python")
    assert python == python_copy
    assert python != java


def test_vacancy_attributes(sample_vacancies):
    """Тестирование атрибутов вакансии"""
    vacancy = sample_vacancies[0]
    assert vacancy.name == "Python Developer"
    assert vacancy.alternate_url == "https://hh.ru/vacancy/1"
    assert vacancy.salary_from == 100000
    assert vacancy.salary_to == 150000
    assert vacancy.requirement == "Python experience"


def test_invalid_salary():
    """Тестирование обработки невалидных зарплат"""
    invalid_vacancy = Vacancy("Invalid", "url", "abc", None, "desc")
    assert invalid_vacancy.salary_from == 0
    assert invalid_vacancy.salary_to == 0


def test_main_data(sample_vacancies):
    """Тестирование метода main_data()"""
    data = sample_vacancies[0].main_data()
    assert data == {
        "name": "Python Developer",
        "alternate_url": "https://hh.ru/vacancy/1",
        "salary_from": 100000,
        "salary_to": 150000,
        "snippet": {"requirement": "Python experience"},
    }