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
Ключевые изменения:

Импорт Vacancy из external_api и hh_class с алиасами для избежания конфликта имен.

Использование filter_vacancies вместо несуществующей filter_word.

Удаление несуществующего импорта HH_API.

Добавление примеров использования всех основных классов и функций.

Эта версия main.py теперь полностью соответствует коду в модулях и может использоваться как точка входа в приложение.

Есть ошибки flake8 (неиспользуемые импорты)
исправь пожалуйста
Вот исправленная версия main.py с удалением неиспользуемых импортов и соответствием flake8:

python
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

    # Сохранение в JSON
    saver = JSONSaver(vacancy_data)
    saver.save_to_file()

    # Добавление отдельной вакансии (пример с использованием данных напрямую)
    example_vacancy = {
        "name": "Python Developer",
        "alternate_url": "https://example.com/python",
        "salary_from": 100000,
        "salary_to": 150000,
        "snippet": {"requirement": "Experience with Python and Django"},
    }
    saver.add_vacancy(example_vacancy)


if __name__ == "__main__":
    main()
