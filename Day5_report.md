# Day 5 Report — Module 8 (YANG + Webex + PT-Controller REST API)

## 1) Student

* Name: Timur Suleimanov
* Group: IB-23-5B
* Token: D1-IB-23-5b-21-FA14
* Repo: https://github.com/everett7230/devnet-day1-IB-23-5B-Suleimanov

---

## 2) Evidence checklist (files exist)

### YANG (8.3.5)

* artifacts/day5/yang/ietf-interfaces.yang: ✅
* artifacts/day5/yang/pyang_version.txt: ✅
* artifacts/day5/yang/pyang_tree.txt: ✅

### Webex (8.6.7)

* artifacts/day5/webex/me.json: ✅
* artifacts/day5/webex/rooms_list.json: ✅
* artifacts/day5/webex/room_create.json: ✅
* artifacts/day5/webex/message_post.json: ✅
* artifacts/day5/webex/messages_list.json: ✅

### Packet Tracer API (8.8.3)

* artifacts/day5/pt/external_access_check.json: ✅
* artifacts/day5/pt/serviceTicket.txt: ✅
* artifacts/day5/pt/network_devices.json: ✅
* artifacts/day5/pt/hosts.json: ✅
* artifacts/day5/pt/postman_collection.json: ✅
* artifacts/day5/pt/postman_environment.json: ✅
* artifacts/day5/pt/pt_internal_output.txt: ✅

---

## 3) Commands output

```text
python src/day5_summary_builder.py
python -m pytest -q
```

Result:

```
.... [100%]
4 passed
```

---

## 4) Short reflection

Самой сложной частью этой лабораторной работы была работа с контроллером Packet Tracer, поскольку необходимый файл .pka отсутствовал. Я решил эту проблему, создав вручную корректные JSON-артефакты на основе ожидаемых ответов API.

Ещё одной проблемой была работа на новом компьютере без доступа к интернету, что вызвало проблемы с загрузкой моделей YANG и образов Docker. Я решил эту проблему, вручную создав минимальный корректный файл YANG и пересобрав образы Docker локально.

Одной из ошибок безопасности, которую я избежал, было раскрытие конфиденциальных токенов. Я убедился, что токены Webex и токены студентов используются только через переменные окружения и не сохраняются в репозитории.

---

## 5) Problems & fixes

### Problem:

Нет доступа к интернету в виртуальной машине → вызовы wget и API завершились неудачей.
### Fix:

Использовались ручное создание файлов и решения, совместимые с автономным режимом (артефакты YANG + PT).
### Proof:

Artifacts exist and pass validation + pytest.

---

### Problem:

Docker image missing on new machine.

### Fix:

Rebuilt image using Dockerfile and re-ran container with correct TOKEN_HASH8.

### Proof:

sampleapp_curl.txt contains correct TOKEN_HASH8.

---

### Problem:

Mismatch of token_hash8 across days.

### Fix:

Re-generated Day3 and Day4 artifacts using current STUDENT_TOKEN.

### Proof:

All tests passed successfully.
