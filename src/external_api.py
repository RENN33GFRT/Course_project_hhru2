class Vacancy:
    """Класс для представления вакансий"""

    __slots__ = ("__title", "vacancy_url", "salary_from", "salary_to", "description")

    def __init__(self, title: str, vacancy_url: str, salary_from: int, salary_to: int, description: str):
        self.__title = title
        self.vacancy_url = vacancy_url
        self.salary_from = self._validate_salary(salary_from)
        self.salary_to = self._validate_salary(salary_to)
        self.description = description

    @property
    def name(self) -> str:
        """Алиас для title (чтобы соответствовать тестам)"""
        return self.__title

    @property
    def title(self) -> str:
        return self.__title

    def _validate_salary(self, salary_value: int) -> int:
        """Проверяет корректность значения зарплаты"""
        if isinstance(salary_value, (int, float)) and salary_value > 0:
            return int(salary_value)
        return 0

    def get_vacancy_data(self) -> dict:
        """Возвращает данные вакансии в виде словаря"""
        return {
            "title": self.__title,
            "url": self.vacancy_url,
            "min_salary": self.salary_from,
            "max_salary": self.salary_to,
            "requirements": self.description,
        }

    def main_data(self) -> dict:
        """Возвращает основные данные вакансии в формате для теста"""
        return {
            "name": self.__title,
            "alternate_url": self.vacancy_url,
            "salary_from": self.salary_from,
            "salary_to": self.salary_to,
            "snippet": {"requirement": self.description},
        }

    def __str__(self) -> str:
        """Строковое представление вакансии"""
        return f"""
        ========================================================================
        Название: {self.__title}
        Ссылка: {self.vacancy_url}
        Зарплата от {self.salary_from} до {self.salary_to}
        Описание: {self.description}
        ========================================================================
        """

    # Методы сравнения вакансий по зарплате
    def __eq__(self, other):
        return self.salary_from == other.salary_from

    def __ne__(self, other):
        return self.salary_from != other.salary_from

    def __lt__(self, other):
        return self.salary_from < other.salary_from

    def __gt__(self, other):
        return self.salary_from > other.salary_from

    def __le__(self, other):
        return self.salary_from <= other.salary_from

    def __ge__(self, other):
        return self.salary_from >= other.salary_from
