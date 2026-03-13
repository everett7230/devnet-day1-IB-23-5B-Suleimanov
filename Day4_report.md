# Day 4 Report — Labs 6–7 (Docker + Jenkins + Security + Ansible)

## 1) Student

* Name: Сулейманов Тимур
* Group: ИБ-23-5б
* Token: D1-IB23-5b-21-FA14
* Repo: https://github.com/everett7230/devnet-day1-IB-23-5B-Suleimanov

---

## 2) Evidence checklist (files exist)

### Docker (6.2.7)

* artifacts/day4/docker/sampleapp_curl.txt: Yes
* artifacts/day4/docker/sampleapp_token_proof.txt: Yes
* artifacts/day4/docker/sampleapp_docker_ps.txt: Yes
* artifacts/day4/docker/sampleapp_build_log.txt: Yes

### Jenkins (6.3.6)

* artifacts/day4/jenkins/jenkins_docker_ps.txt: Yes
* artifacts/day4/jenkins/buildapp_console.txt: Yes
* artifacts/day4/jenkins/testapp_console.txt: Yes
* artifacts/day4/jenkins/pipeline_script.groovy: Yes
* artifacts/day4/jenkins/pipeline_console.txt: Yes
* artifacts/day4/jenkins/jenkins_url.txt: Yes

### Ansible (7.4.8)

* artifacts/day4/ansible/ansible_ping.txt: Yes
* artifacts/day4/ansible/ansible_hello.txt: Yes
* artifacts/day4/ansible/ansible_playbook_install.txt: Yes
* artifacts/day4/ansible/ports_conf_after.txt: Yes
* artifacts/day4/ansible/curl_apache_8081.txt: Yes

### Security (6.5.10)

* artifacts/day4/security/signup_v1.txt: Yes
* artifacts/day4/security/login_v1.txt: Yes
* artifacts/day4/security/signup_v2.txt: Yes
* artifacts/day4/security/login_v2.txt: Yes
* artifacts/day4/security/db_tables.txt: Yes
* artifacts/day4/security/db_user_hash_sample.txt: Yes

---

## 3) Commands output

```text
python src/day4_summary_builder.py
pytest -q
```

---

## 4) Short reflection (5–8 lines)

В ходе выполнения лабораторной работы Day 4 были изучены инструменты автоматизации и DevOps-процессы.
Наиболее интересной частью была работа с Docker и Jenkins, поскольку они позволяют автоматизировать сборку и тестирование приложений.
Docker позволил создать изолированную среду для запуска веб-приложения, а Jenkins был использован для построения CI/CD pipeline.
Также был изучен Ansible для автоматической установки и настройки веб-сервера Apache.
Дополнительно была рассмотрена эволюция методов хранения паролей и различия между хранением паролей в открытом виде и в виде хешей.
Полученные навыки позволяют лучше понять процессы автоматизации разработки и повышения безопасности приложений.

---

## 5) Problems & fixes (at least 1)

Проблема:
При выполнении Jenkins pipeline некоторые этапы initially не отображались в Console Output.

Fix:
Pipeline script был перепроверен и перезапущен job в Jenkins, после чего стадии **Preparation**, **Build** и **Results** корректно появились в выводе.

Proof:
В файле `artifacts/day4/jenkins/pipeline_console.txt` присутствуют стадии pipeline и финальный статус выполнения.
