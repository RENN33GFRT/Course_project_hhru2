class Vacancy:
    """Класс для представления вакансий"""

    __slots__ = ("__title", "vacancy_url", "min_salary", "max_salary", "description")

    def __init__(self, title: str, vacancy_url: str, min_salary: int, max_salary: int, description: str):
        self.__title = title
        self.vacancy_url = vacancy_url
        self.min_salary = self._validate_salary(min_salary)
        self.max_salary = self._validate_salary(max_salary)
        self.description = description

    @property
    def title(self) -> str:
        return self.__title

    def _validate_salary(self, salary_value: int) -> int:
        """Проверяет корректность значения зарплаты"""
        if isinstance(salary_value, (int, float)) and salary_value > 0:
            return salary_value
        return 0

    def get_vacancy_data(self) -> dict:
        """Возвращает данные вакансии в виде словаря"""
        return {
            "title": self.__title,
            "url": self.vacancy_url,
            "min_salary": self.min_salary,
            "max_salary": self.max_salary,
            "requirements": self.description,
        }

    def __str__(self) -> str:
        """Строковое представление вакансии"""
        return f"""
        ========================================================================
        Вакансия: {self.__title}
        Ссылка: {self.vacancy_url}
        Зарплата: от {self.min_salary} до {self.max_salary}
        Требования: {self.description}
        ========================================================================
        """

    # Методы сравнения вакансий по зарплате
    def __eq__(self, other):
        return self.min_salary == other.min_salary

    def __ne__(self, other):
        return self.min_salary != other.min_salary

    def __lt__(self, other):
        return self.min_salary < other.min_salary

    def __gt__(self, other):
        return self.min_salary > other.min_salary

    def __le__(self, other):
        return self.min_salary <= other.min_salary

    def __ge__(self, other):
        return self.min_salary >= other.min_salary