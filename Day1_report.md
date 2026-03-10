# Day 1 Report — DevNet Sprint

## 1. Student
- Name: Сулейманов Тимур
- Group: ИБ-22-3б
- GitHub repo: https://github.com/everett7230/devnet-day1-IB-23-5B-Suleimanov.git
- Day1 Token: D1-IB-23-5b-21-FA14

## 2. NetAcad progress (Module 1)
- Completed items: 1.1 / 1.2 / 1.3
- Screenshot(s):
  - Скриншот прогресса NetAcad

## 3. VM evidence
- File: `artifacts/day1/env.txt` exists: Yes
- Screenshot(s):
  - Скриншот терминала в DEVASC VM с `hostnamectl` и `date -u`

## 4. Repo structure (must match assignment)
- `src/day1_api_hello.py` : Yes
- `tests/test_day1_api_hello.py` : Yes
- `schemas/day1_summary.schema.json` : Yes
- `artifacts/day1/summary.json` : Yes
- `artifacts/day1/response.json` : Yes

## 5. Commands run (paste EXACT output)
### 5.1 Script run
```text
[сюда вставь вывод команды: python src/day1_api_hello.py]
python src/day1_api_hello.py
{
  "schema_version": "1.0",
  "generated_utc": "2026-03-10T11:03:38.510454+00:00",
  "student": {
    "token": "D1-IB23-5b-21-FA14",
    "name": "Сулейманов Тимур",
    "group": "ИБ-23-5б"
  },
  "api": {
    "url": "https://jsonplaceholder.typicode.com/todos/1",
    "status_code": 200,
    "validation_passed": true,
    "validation_errors": [],
    "response_sha256": "ffefdf50d54770c2a20ba143e42daa910535c20ec5ca7a1e449dac71729f00fe"
  },
  "run": {
    "python": "3.8.2",
    "platform": "linux"
  }
}


## 6. Что я изучил сегодня (3–6 bullets)

 Научился запускать и работать в DEVASC VM через VirtualBox.
 Научился создавать репозиторий на GitHub и работать с Git.
 Научился создавать и использовать виртуальное окружение Python (venv).
 Научился отправлять HTTP GET запрос к API с помощью библиотеки requests.
 Научился сохранять ответ API в JSON и считать SHA256.
 Научился запускать тесты с помощью pytest.

## 7. Проблемы и решения

- Problem:
Во время выполнения скрипта появилась ошибка.
- Fix:


Я исправил код и после этого скрипт начал работать.
python src/day1_api_hello.py
Traceback (most recent call last):
  File "src/day1_api_hello.py", line 74, in <module>
    def fetch_online(url: str, timeout: int = 10) -> tuple[int, dict]:
TypeError: 'type' object is not subscriptable
Также была проблема с подключением и с содержанием env
Все было успешно исправлено с помощью корректной правки и проверкой 
- Proof:
Скрипт успешно запускается командой:
python src/day1_api_hello.py
результат проверки выше

Тесты проходят командой:
pytest -q

Также была ошибка с загрузкой файлов на репозиторий в гит
Успешно починил с помощью PAT ключа 
