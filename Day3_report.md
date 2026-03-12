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
