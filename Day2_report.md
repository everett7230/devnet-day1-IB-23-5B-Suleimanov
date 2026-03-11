# Day 2 Report — Git + Data Formats + Tests

## 1) Student
- Name: Сулейманов Тимур
- Group: ИБ-23-5б
- Token: D1-IB23-5b-21-FA14
- Repo: https://github.com/everett7230/devnet-day1-IB-23-5B-Suleimanov
- PR link (day2): https://github.com/everett7230/devnet-day1-IB-23-5B-Suleimanov/pull/1

## 2) NetAcad progress
- Module 2.2 done: Yes (screenshot added)
- Module 3.1–3.6 done: Yes (screenshot added)

## 3) Git evidence
- File artifacts/day2/git_log.txt exists: Yes
- File artifacts/day2/conflict_log.txt exists: Yes

Conflict note:
Во время выполнения задания возник конфликт в файле README.md. Я открыл файл, удалил конфликтующие строки и оставил правильный текст, после чего сделал commit.

## 4) Generated artifacts (Day2)
- normalized.json: Yes
- normalized.yaml: Yes
- normalized.xml: Yes
- normalized.csv: Yes
- summary.json: Yes

## 5) Commands output (paste EXACT output)

### 5.1 Generator

```text
python src/day2_data_formats.py --input artifacts/day1/response.json

{
  "schema_version": "2.0",
  "generated_utc": "2026-03-11T09:59:03.039349+00:00",
  "student": {
    "token": "D1-IB23-5b-21-FA14",
    "token_hash8": "935cc981",
    "name": "Сулейманов Тимур",
    "group": "ИБ-23-5б"
  },
  "computed": {
    "title_len": 18
  }
}
```

### 5.2 Tests
```pytest -q```

.
1 passed in 0.22s

## 6) What I learned
- Научился работать с ветками Git.
- Научился создавать Pull Request на GitHub.
- Научился решать merge conflict.
- Научился работать с форматами данных JSON, YAML, XML и CSV.
- Научился писать тесты и запускать pytest.

## 7) Problems & fixes

Problem:
Во время выполнения задания возник merge conflict в файле README.md.

Fix:
Я открыл файл README.md, исправил конфликтующие строки и сделал commit с сообщением:

Resolve README conflict (Day2)

Proof:
Файлы доказательства:
artifacts/day2/conflict_log.txt
artifacts/day2/git_log.txt
