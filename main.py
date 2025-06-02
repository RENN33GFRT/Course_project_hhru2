from src.external_api import API_HH
from src.filter import filter_word
from src.hh_class import Vacancy
from src.saver_class import File_Save


def main():
    """Основная программа где происходят почти все действия с классами и функциями"""
    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий (через пробел): ").split()

    api = API_HH()
    vacancies = api.get_vacancies(search_query, top_n)
    saver = File_Save(vacancies)
    saver.save_to_file()
    vacancies["items"] = filter_word(vacancies, filter_words)

    for i in vacancies["items"]:
        salary_from = 0
        salary_to = 0
        if i.get("salary"):
            salary_from = i["salary"].get("from") or 0
            salary_to = i["salary"].get("to") or 0

        vacancy = Vacancy(i["name"], i["alternate_url"], salary_from, salary_to, i["snippet"]["requirement"])
        print(vacancy)


main()