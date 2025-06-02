from typing import Union
import re


def filter_vacancies(vacancies_data: dict, filter_words: list) -> Union[list, dict]:
    """Фильтрует вакансии по ключевым словам в описании"""
    filtered_vacancies = []

    if not filter_words:
        return vacancies_data["items"]

    for vacancy in vacancies_data["items"]:
        try:
            requirements = vacancy["snippet"]["requirement"]
            if not requirements:  # Если requirements None или пустая строка
                continue

            # Создаем регулярное выражение для поиска целых слов
            pattern = r'\b(?:{})\b'.format('|'.join(map(re.escape, filter_words)))
            if re.search(pattern, requirements, flags=re.IGNORECASE):
                filtered_vacancies.append(vacancy)
        except (KeyError, TypeError):
            continue

    return filtered_vacancies