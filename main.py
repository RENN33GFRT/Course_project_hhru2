from src.external_api import Vacancy as ExternalVacancy
from src.hh_class import Vacancy as HHVacancy
from src.filter import filter_vacancies
from src.saver_class import JSONSaver


def main():
    # Пример использования классов и функций
    vacancy_data = {
        "items": [
            {
                "name": "Python Developer",
                "alternate_url": "https://example.com/python",
                "salary_from": 100000,
                "salary_to": 150000,
                "snippet": {"requirement": "Experience with Python and Django"},
            },
            {
                "name": "Java Developer",
                "alternate_url": "https://example.com/java",
                "salary_from": 90000,
                "salary_to": 120000,
                "snippet": {"requirement": "Experience with Java and Spring"},
            },
        ]
    }

    # Фильтрация вакансий
    filtered = filter_vacancies(vacancy_data, ["Python", "Django"])
    print("Отфильтрованные вакансии:", filtered)

    # Создание объектов Vacancy
    external_vacancy = ExternalVacancy(
        title="Python Developer",
        vacancy_url="https://example.com/python",
        salary_from=100000,
        salary_to=150000,
        description="Experience with Python and Django",
    )

    hh_vacancy = HHVacancy(
        name="Python Developer",
        alternate_url="https://example.com/python",
        salary_from=100000,
        salary_to=150000,
        requirement="Experience with Python and Django",
    )

    # Сохранение в JSON
    saver = JSONSaver(vacancy_data)
    saver.save_to_file()

    # Добавление отдельной вакансии
    saver.add_vacancy(hh_vacancy.main_data())


if __name__ == "__main__":
    main()
