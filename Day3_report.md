# Day 3 Report — Lab 4.5.5 + Auto-check artifacts

## 1) Student

* Name: Сулейманов Тимур
* Group: ИБ-23-5б
* Token: D1-IB23-5b-21-FA14
* Repo: https://github.com/everett7230/devnet-day1-IB-23-5B-Suleimanov

---

## 2) Lab 4.5.5 completion evidence

* API docs (Try it out) screenshots: выполнены GET /books и другие запросы через Try it out
* Postman screenshots: выполнены запросы GET /books, POST /loginViaBasic, POST /books
* Python run screenshot: выполнен скрипт добавления 100 книг и запуск pytest

---

## 3) Artifacts checklist

* artifacts/day3/books_before.json: Yes
* artifacts/day3/books_sorted_isbn.json: Yes
* artifacts/day3/mybook_post.json: Yes
* artifacts/day3/books_by_me.json: Yes
* artifacts/day3/add100_report.json: Yes
* artifacts/day3/postman_collection.json: Yes
* artifacts/day3/postman_environment.json: Yes
* artifacts/day3/curl_get_books.txt: Yes
* artifacts/day3/curl_get_books_isbn.txt: Yes
* artifacts/day3/curl_get_books_sorted.txt: Yes
* artifacts/day3/summary.json: Yes

---

## 4) Command outputs (paste exact)

### 4.1 Script run

```text
python src/day3_library_lab.py --count 100
```

```text
devasc@labvm:~/devnet-day1-IB-23-5B-Suleimanov$ python3 src/day3_library_lab.py --count 100
{
  "schema_version": "3.1",
  "generated_utc": "2026-03-12T17:17:01.781631+00:00",
  "student": {
    "token": "D1-IB23-5b-21-FA14",
    "token_hash8": "935cc981",
    "name": "Сулейманов Тимур",
    "group": "ИБ-23-5б"
  },
  "lab": {
    "apihost": "http://library.demo.local",
    "must_use": {
      "login_endpoint": "http://library.demo.local/api/v1/loginViaBasic",
      "books_endpoint": "http://library.demo.local/api/v1/books",
      "api_key_header": "X-API-KEY"
    }
  },
  "artifacts_sha256": {
    "books_before": "e9d34fda886ea13e48f880ed70831f5548107833a76bb9f8888b88bb5c979458",
    "books_sorted_isbn": "93934547f1e3d0d592639533661497ca2eb6a8b60073b0bfd7fecc086edf0d6b",
    "mybook_post": "60321524127a846f25fb803aefffe1b56cee912ac89befb0a68ba68736e1ef53",
    "books_by_me": "05357496d061f41eb8222c70da67341f46fe8d955144fdf23c193f5b55377141",
    "add100_report": "93db862eb191e2f05f706577c871a606b78086e86a0055c5aaa0a351fa35571a",
    "postman_collection": "0304093b71dd9acdc4b0398123efaec14b60aeb86e4e2626ea3633c05d13b506",
    "postman_environment": "21ff9a78a289a7c313d1db40795ede7b6320d959fd56981a2e3855e2d5bbef7f",
    "curl_get_books": "398021a314dd5db8b544000199104b769a7afcc63fa3cfa531f306c36cc49518",
    "curl_get_books_isbn": "2ec02f0cfbf0e06b9b7254807dc91362f08663528bb8290ca45092798b81f9bd",
    "curl_get_books_sorted": "d628b2e92e81dcc32d34656bfc85ce21b15435096b7f8064423ba37b96568e50"
  },
  "validation": {
    "must_have_mybook_title_contains_token_hash8": true,
    "must_have_added_100": true
  }
}
```

Скрипт успешно выполнил следующие действия:

* получил API token через endpoint `/loginViaBasic`
* добавил уникальную книгу пользователя
* сгенерировал 100 книг с помощью библиотеки faker
* добавил книги через REST API
* выполнил проверку через фильтр `author`
* создал artifacts и файл `summary.json`

---

### 4.2 Tests

```text
pytest -q
```

Output:

```text
1 passed
```

---

## 5) Problems & fixes (at least 1)

Проблема:
При выполнении запроса **POST /books** в Postman возникала ошибка:

```
Input payload validation failed
None is not of type 'object'
```

Причина:
Тело запроса было отправлено в формате **Text**, а не **JSON**.

Исправление:
Тип тела запроса был изменён на:

```
Body → raw → JSON
```

После изменения формата запрос был успешно выполнен и книга была добавлена в систему.

Proof:
Запрос успешно выполнился, книга появилась в API и Python скрипт смог добавить книги без ошибок.
