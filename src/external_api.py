from abc import ABC, abstractmethod
import requests


class BaseAPI(ABC):
    """Абстрактный базовый класс для API сервисов"""

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __connect(self) -> bool:
        """Проверка соединения с API"""
        pass

    @abstractmethod
    def get_vacancies(self, search_query: str, top_n: int = 100) -> dict:
        """Получение вакансий по поисковому запросу"""
        pass


class HeadHunterAPI(BaseAPI):
    """Реализация API для HeadHunter"""

    def __init__(self):
        self.__api_url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}

    def _BaseAPI__connect(self) -> bool:
        """Проверка доступности API HH"""
        try:
            response = requests.get(self.__api_url, headers=self.__headers)
            return response.status_code == 200
        except requests.RequestException:
            return False

    def get_vacancies(self, search_query: str, top_n: int = 100) -> dict | None:
        """
        Получение вакансий с HH API
        :param search_query: Поисковый запрос
        :param top_n: Количество возвращаемых вакансий
        :return: Словарь с вакансиями или None при ошибке
        """
        if not self._BaseAPI__connect():
            print(f"Сервер недоступен. Код ошибки: {requests.get(self.__api_url).status_code}")
            return None

        params = {
            "text": search_query,
            "per_page": top_n,
            "search_field": "name",
            "page": 0
        }

        try:
            response = requests.get(
                url=self.__api_url,
                params=params,
                headers=self.__headers
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Ошибка при запросе к API: {e}")
            return None


class BaseVacancy(ABC):
    """Базовый абстрактный класс для работы с вакансиями"""

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_vacancy_data(self) -> dict:
        """Возвращает данные вакансии в виде словаря"""
        pass

    @abstractmethod
    def validate_salary(self, salary_value: int) -> int:
        """Проверяет корректность значения зарплаты"""
        pass


class Vacancy(BaseVacancy):
    """Класс для представления и работы с вакансиями"""

    __slots__ = ("__title", "vacancy_url", "salary_from", "salary_to", "description")

    def __init__(self, title: str, vacancy_url: str,
                 salary_from: int, salary_to: int, description: str):
        """
        Инициализация объекта вакансии

        :param title: Название вакансии
        :param vacancy_url: Ссылка на вакансию
        :param salary_from: Зарплата от
        :param salary_to: Зарплата до
        :param description: Описание вакансии
        """
        self.__title = title
        self.vacancy_url = vacancy_url
        self.salary_from = self.validate_salary(salary_from)
        self.salary_to = self.validate_salary(salary_to)
        self.description = description

    @property
    def name(self) -> str:
        """Алиас для title (чтобы соответствовать тестам)"""
        return self.__title

    @property
    def title(self) -> str:
        """Возвращает название вакансии"""
        return self.__title

    def validate_salary(self, salary_value: int) -> int:
        """
        Проверяет корректность значения зарплаты

        :param salary_value: Значение зарплаты
        :return: Проверенное значение или 0 если невалидно
        """
        if isinstance(salary_value, (int, float)) and salary_value > 0:
            return int(salary_value)
        return 0

    def get_vacancy_data(self) -> dict:
        """
        Возвращает данные вакансии в виде словаря

        :return: Словарь с данными вакансии
        """
        return {
            "title": self.__title,
            "url": self.vacancy_url,
            "min_salary": self.salary_from,
            "max_salary": self.salary_to,
            "requirements": self.description,
        }

    def get_main_data(self) -> dict:
        """
        Возвращает основные данные вакансии в формате для теста

        :return: Словарь с основными данными вакансии
        """
        return {
            "name": self.__title,
            "alternate_url": self.vacancy_url,
            "salary_from": self.salary_from,
            "salary_to": self.salary_to,
            "snippet": {"requirement": self.description},
        }

    def __str__(self) -> str:
        """
        Строковое представление вакансии

        :return: Форматированная строка с данными вакансии
        """
        return f"""
        ========================================================================
        Название: {self.__title}
        Ссылка: {self.vacancy_url}
        Зарплата от {self.salary_from} до {self.salary_to}
        Описание: {self.description}
        ========================================================================
        """

    # Методы сравнения вакансий по зарплате
    def __eq__(self, other: 'Vacancy') -> bool:
        if not isinstance(other, Vacancy):
            raise TypeError("Сравнение возможно только между объектами Vacancy")
        return self.salary_from == other.salary_from

    def __ne__(self, other: 'Vacancy') -> bool:
        if not isinstance(other, Vacancy):
            raise TypeError("Сравнение возможно только между объектами Vacancy")
        return self.salary_from != other.salary_from

    def __lt__(self, other: 'Vacancy') -> bool:
        if not isinstance(other, Vacancy):
            raise TypeError("Сравнение возможно только между объектами Vacancy")
        return self.salary_from < other.salary_from

    def __gt__(self, other: 'Vacancy') -> bool:
        if not isinstance(other, Vacancy):
            raise TypeError("Сравнение возможно только между объектами Vacancy")
        return self.salary_from > other.salary_from

    def __le__(self, other: 'Vacancy') -> bool:
        if not isinstance(other, Vacancy):
            raise TypeError("Сравнение возможно только между объектами Vacancy")
        return self.salary_from <= other.salary_from

    def __ge__(self, other: 'Vacancy') -> bool:
        if not isinstance(other, Vacancy):
            raise TypeError("Сравнение возможно только между объектами Vacancy")
        return self.salary_from >= other.salary_from
