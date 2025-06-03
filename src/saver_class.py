import json
import os
from abc import ABC, abstractmethod
from typing import Any


class BaseSaver(ABC):
    @abstractmethod
    def save_to_file(self):
        pass

    @abstractmethod
    def read_file(self):
        pass

    @abstractmethod
    def clear_file(self):
        pass

    @abstractmethod
    def add_vacancy(self, vacancy_data):
        pass


class JSONSaver(BaseSaver):
    def __init__(self, vacancies_data: dict, filename: str = "vacancies"):
        self.vacancies_data = vacancies_data
        self.__filename = f"{filename}.json" if not filename.endswith('.json') else filename
        self.__ensure_directory_exists()

    def __ensure_directory_exists(self):
        """Создает директорию, если она не существует"""
        os.makedirs(os.path.dirname(self.__filename), exist_ok=True)

    def read_file(self) -> dict:
        try:
            with open(self.__filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {"vacancies": []}

    def save_to_file(self):
        data = self.read_file()
        if not isinstance(data, dict):
            data = {"vacancies": []}

        # Добавляем новые вакансии
        new_vacancies = []
        for vacancy in self.vacancies_data.get("items", []):
            if not any(v.get("alternate_url") == vacancy.get("alternate_url")
                       for v in data.get("vacancies", [])):
                new_vacancies.append(vacancy)

        data["vacancies"].extend(new_vacancies)

        with open(self.__filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def clear_file(self):
        with open(self.__filename, 'w', encoding='utf-8') as f:
            json.dump({"vacancies": []}, f)

    def add_vacancy(self, vacancy_data: dict):
        if not isinstance(vacancy_data, dict):
            print("Можно добавлять только main_data из класса Vacancy")
            return

        data = self.read_file()
        if not any(v == vacancy_data for v in data.get("vacancies", [])):
            data["vacancies"].append(vacancy_data)
            with open(self.__filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)