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
        return (
            "    =========================================================================\n"
            f"    Название: {self.name}\n"
            f"    Ссылка: {self.alternate_url}\n"
            f"    Зарплата от {self.salary_from} до {self.salary_to}\n"
            f"    Описание: {self.requirement}\n"
            "    ========================================================================="
        )

    # Полная реализация методов сравнения
    def __eq__(self, other):
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary_from == other.salary_from

    def __ne__(self, other):
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary_from != other.salary_from

    def __lt__(self, other):
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary_from < other.salary_from

    def __gt__(self, other):
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary_from > other.salary_from

    def __le__(self, other):
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary_from <= other.salary_from

    def __ge__(self, other):
        if not isinstance(other, Vacancy):
            return NotImplemented
        return self.salary_from >= other.salary_from
