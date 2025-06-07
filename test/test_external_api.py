import pytest
from unittest.mock import patch, MagicMock
from src.external_api import BaseAPI, HeadHunterAPI, Vacancy
import requests


class TestBaseAPI:
    """Тесты для базового абстрактного класса API"""

    def test_base_api_is_abstract(self):
        """Проверяет, что BaseAPI действительно абстрактный класс"""
        with pytest.raises(TypeError):
            BaseAPI()


class TestHeadHunterAPI:
    """Тесты для класса HeadHunterAPI"""

    @pytest.fixture
    def hh_api(self):
        """Фикстура для создания экземпляра API"""
        return HeadHunterAPI()

    def test_init(self, hh_api):
        """Проверяет инициализацию API"""
        assert hasattr(hh_api, "_HeadHunterAPI__api_url")
        assert hh_api._HeadHunterAPI__api_url == "https://api.hh.ru/vacancies"
        assert hasattr(hh_api, "_HeadHunterAPI__headers")

    @patch('requests.get')
    def test_connect_success(self, mock_get, hh_api):
        """Проверяет успешное соединение с API"""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        assert hh_api._BaseAPI__connect() is True
        mock_get.assert_called_once_with(
            "https://api.hh.ru/vacancies",
            headers={"User-Agent": "HH-User-Agent"}
        )

    @patch('requests.get')
    def test_connect_failure(self, mock_get, hh_api):
        """Проверяет неудачное соединение с API"""
        mock_get.side_effect = requests.RequestException("Connection error")
        assert hh_api._BaseAPI__connect() is False

    @patch.object(HeadHunterAPI, '_BaseAPI__connect')
    @patch('requests.get')
    def test_get_vacancies_success(self, mock_get, mock_connect, hh_api):
        """Проверяет успешное получение вакансий"""
        mock_connect.return_value = True
        mock_response = MagicMock()
        mock_response.json.return_value = {"items": [{"id": "1"}]}
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        result = hh_api.get_vacancies("python", 10)
        assert result == {"items": [{"id": "1"}]}

    @patch.object(HeadHunterAPI, '_BaseAPI__connect')
    def test_get_vacancies_connection_failed(self, mock_connect, hh_api):
        """Проверяет поведение при неудачном соединении"""
        mock_connect.return_value = False
        assert hh_api.get_vacancies("python") is None


class TestVacancy:
    """Тесты для класса Vacancy"""

    @pytest.fixture
    def vacancy(self):
        """Фикстура для создания тестовой вакансии"""
        return Vacancy(
            title="Python Developer",
            vacancy_url="http://example.com",
            salary_from=100000,
            salary_to=150000,
            description="Требуется Python разработчик"
        )

    def test_vacancy_creation(self, vacancy):
        """Проверяет корректность создания вакансии"""
        assert vacancy.title == "Python Developer"
        assert vacancy.vacancy_url == "http://example.com"
        assert vacancy.salary_from == 100000
        assert vacancy.salary_to == 150000
        assert vacancy.description == "Требуется Python разработчик"

    def test_validate_salary(self, vacancy):
        """Проверяет валидацию зарплаты"""
        assert vacancy.validate_salary(100000) == 100000
        assert vacancy.validate_salary("100000") == 0
        assert vacancy.validate_salary(-100000) == 0
        assert vacancy.validate_salary(0) == 0

    def test_get_vacancy_data(self, vacancy):
        """Проверяет преобразование в словарь"""
        expected = {
            "title": "Python Developer",
            "url": "http://example.com",
            "min_salary": 100000,
            "max_salary": 150000,
            "requirements": "Требуется Python разработчик"
        }
        assert vacancy.get_vacancy_data() == expected

    def test_comparison_operators(self):
        """Проверяет операторы сравнения"""
        v1 = Vacancy("Dev 1", "url1", 100000, 150000, "Desc 1")
        v2 = Vacancy("Dev 2", "url2", 120000, 180000, "Desc 2")

        assert v1 < v2
        assert v2 > v1
        assert v1 != v2
        assert v1 == Vacancy("Dev 3", "url3", 100000, 200000, "Desc 3")