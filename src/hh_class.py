class Vacancy:
    """Класс для представления вакансий"""

    def __init__(self, name: str, alternate_url: str, salary_from: int, salary_to: int, requirement: str):
        self.name = name
        self.alternate_url = alternate_url
        self.salary_from = self._validate_salary(salary_from)
        self.salary_to = self._validate_salary(salary_to)
        self.requirement = requirement

    def _validate_salary(self, salary_value) -> int:
        """Проверяет корректность значения зарплаты"""
        try:
            salary = int(salary_value)
            return salary if salary > 0 else 0
        except (ValueError, TypeError):
            return 0

    def main_data(self) -> dict:
        """Возвращает основные данные вакансии"""
        return {
            "name": self.name,
            "alternate_url": self.alternate_url,
            "salary_from": self.salary_from,
            "salary_to": self.salary_to,
            "snippet": {"requirement": self.requirement},
        }

    def __str__(self) -> str:
        """Строковое представление вакансии"""
        return f"""
        ========================================================================
        Название: {self.name}
        Ссылка: {self.alternate_url}
        Зарплата от {self.salary_from} до {self.salary_to}
        Описание: {self.requirement}
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