import json
import os
from abc import ABC, abstractmethod
from src.hh_class import Vacancy


class BaseSaver(ABC):  # pragma: no cover
    """Абстрактный класс для сохранения данных"""

    @abstractmethod
    def __init__(self, vacancies_data, filename="vacancies"):
        pass

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
    """Класс для работы с вакансиями в JSON-файле"""

    def __init__(self, vacancies_data: dict, filename: str = "vacancies"):
        self.vacancies_data = vacancies_data
        self.__filename = filename

    def read_file(self) -> dict:
        """Читает данные из файла"""
        base_dir = os.path.dirname(os.path.abspath(__file__))
        data_dir = os.path.join(base_dir, "..", "data")
        file_path = os.path.join(data_dir, f"{self.__filename}.json")

        try:
            with open(file_path, encoding="utf-8") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {"vacancies": []}

    def save_to_file(self):
        """Сохраняет вакансии в файл"""
        base_dir = os.path.dirname(os.path.abspath(__file__))
        data_dir = os.path.join(base_dir, "..", "data")
        file_path = os.path.join(data_dir, f"{self.__filename}.json")

        existing_data = self.read_file()
        if not isinstance(existing_data, dict) or 'vacancies' not in existing_data:
            existing_data = {"vacancies": []}

        existing_vacancies = {(item.get("title"), item.get("url")) for item in existing_data['vacancies']}
        new_vacancies = []

        for vacancy in self.vacancies_data["items"]:
            salary_from = vacancy.get("salary", {}).get("from", 0) or 0
            salary_to = vacancy.get("salary", {}).get("to", 0) or 0

            vacancy_obj = Vacancy(
                vacancy["name"],
                vacancy["alternate_url"],
                salary_from,
                salary_to,
                vacancy["snippet"].get("requirement", "")
            )

            vacancy_key = (vacancy_obj.title, vacancy_obj.vacancy_url)
            if vacancy_key not in existing_vacancies:
                new_vacancies.append(vacancy_obj.get_vacancy_data())
                existing_vacancies.add(vacancy_key)

        existing_data['vacancies'].extend(new_vacancies)

        os.makedirs(data_dir, exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(existing_data, file, ensure_ascii=False, indent=2)

    def clear_file(self):
        """Очищает файл с вакансиями"""
        base_dir = os.path.dirname(os.path.abspath(__file__))
        data_dir = os.path.join(base_dir, "..", "data")
        file_path = os.path.join(data_dir, f"{self.__filename}.json")

        os.makedirs(data_dir, exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump({"vacancies": []}, file)

    def add_vacancy(self, vacancy_data: dict):
        """Добавляет одну вакансию в файл"""
        if not isinstance(vacancy_data, dict):
            print("Можно добавлять только main_data из класса Vacancy")
            return

        base_dir = os.path.dirname(os.path.abspath(__file__))
        data_dir = os.path.join(base_dir, "..", "data")
        file_path = os.path.join(data_dir, f"{self.__filename}.json")

        try:
            with open(file_path, encoding="utf-8") as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = {"vacancies": []}

        if not any(v == vacancy_data for v in data["vacancies"]):
            data["vacancies"].append(vacancy_data)

        os.makedirs(data_dir, exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=2)