import pytest
from src.filter import filter_vacancies

@pytest.fixture
def sample_vacancies():
    return {
        "items": [
            {
                "name": "Python Developer",
                "snippet": {
                    "requirement": "Experience with Python and Django",
                    "responsibility": "Develop web applications"
                }
            },
            {
                "name": "Java Developer",
                "snippet": {
                    "requirement": "Java and Spring experience",
                    "responsibility": "Backend development"
                }
            },
            {
                "name": "Frontend Developer",
                "snippet": {
                    "requirement": "JavaScript, React",
                    "responsibility": None
                }
            },
            {
                "name": "DevOps Engineer",
                "snippet": {
                    "requirement": None,
                    "responsibility": "Deploy and maintain infrastructure"
                }
            }
        ]
    }

def test_filter_with_matching_keywords(sample_vacancies):
    """Тест фильтрации с подходящими ключевыми словами"""
    result = filter_vacancies(sample_vacancies, ["python", "django"])
    assert len(result) == 1
    assert result[0]["name"] == "Python Developer"

def test_filter_with_no_matches(sample_vacancies):
    """Тест фильтрации без совпадений"""
    result = filter_vacancies(sample_vacancies, ["ruby"])
    assert len(result) == 0

def test_filter_with_empty_keywords(sample_vacancies):
    """Тест фильтрации с пустым списком ключевых слов"""
    result = filter_vacancies(sample_vacancies, [])
    assert len(result) == len(sample_vacancies["items"])

def test_filter_with_partial_match(sample_vacancies):
    """Тест частичного совпадения"""
    result = filter_vacancies(sample_vacancies, ["java"])
    assert len(result) == 1
    assert result[0]["name"] == "Java Developer"

def test_filter_case_insensitive(sample_vacancies):
    """Тест регистронезависимости"""
    result = filter_vacancies(sample_vacancies, ["PYTHON"])
    assert len(result) == 1
    assert result[0]["name"] == "Python Developer"

def test_filter_with_missing_requirements(sample_vacancies):
    """Тест с вакансией без требований"""
    result = filter_vacancies(sample_vacancies, ["react"])
    assert len(result) == 1
    assert result[0]["name"] == "Frontend Developer"

def test_filter_with_none_requirements(sample_vacancies):
    """Тест с вакансией, где requirements=None"""
    # Добавляем вакансию с None в requirements
    sample_vacancies["items"].append({
        "name": "Test Vacancy",
        "snippet": {
            "requirement": None,
            "responsibility": "Test responsibilities"
        }
    })
    result = filter_vacancies(sample_vacancies, ["test"])
    assert len(result) == 0

def test_filter_with_empty_requirements_string(sample_vacancies):
    """Тест с пустой строкой в требованиях"""
    # Добавляем вакансию с пустой строкой в requirements
    sample_vacancies["items"].append({
        "name": "Empty Requirements",
        "snippet": {
            "requirement": "",
            "responsibility": "Some responsibilities"
        }
    })
    result = filter_vacancies(sample_vacancies, ["empty"])
    assert len(result) == 0