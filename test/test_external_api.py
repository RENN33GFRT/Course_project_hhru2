from abc import ABC, abstractmethod
from typing import Any
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
    def get_vacancies(self, search_query: str, top_n: int = 100) -> Any:
        """Получение вакансий по поисковому запросу"""
        pass


class HeadHunterAPI(BaseAPI):
    """Реализация API для HeadHunter"""

    def __init__(self):
        self.__api_url = "https://api.hh.ru/vacancies"

    def _BaseAPI__connect(self) -> bool:
        """Проверка доступности API HH"""
        try:
            response = requests.get(self.__api_url)
            return response.status_code == 200
        except requests.RequestException:
            return False

    def get_vacancies(self, search_query: str, top_n: int = 100) -> Any:
        """
        Получение вакансий с HH API
        :param search_query: Поисковый запрос
        :param top_n: Количество возвращаемых вакансий
        :return: Список вакансий в формате JSON или None при ошибке
        """
        if not self._BaseAPI__connect():
            status_code = requests.get(self.__api_url).status_code
            print(f"Сервер недоступен. Код ошибки: {status_code}")
            return None

        params = {"text": search_query, "per_page": top_n, "search_field": "name", "page": 0}

        try:
            response = requests.get(url=self.__api_url, params=params, headers={"User-Agent": "HH-User-Agent"})
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Ошибка при запросе к API: {e}")
            return None
