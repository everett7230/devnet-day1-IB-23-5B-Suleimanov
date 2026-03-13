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
{

  "schema_version": "4.1",
  "generated_utc": "2026-03-13T16:00:46.953421+00:00",
  "student": {
    "token": "",
    "token_hash8": "",
    "name": "",
    "group": ""
  },
  "checks": {
    "docker_token_in_page": false,
    "docker_tokenproof": true,
    "ansible_port_8081": true,
    "jenkins_pipeline_has_stages": true,
    "security_db_has_tables": false
  },
  "evidence_sha256": {
    "docker_sampleapp_curl": "47c48c94ef1b1995f5e9b473296e7114a563e2b000661937fe5eda7b78ed1e1d",
    "docker_ps": "1f8dc04fb27429d1642585fd67bcfb712f55f388335437fbd714c44fda82b0df",
    "docker_build_log": "2d5f7a24b5be351fd975d0dd4403c32681a69af70d029ef8d3ed240107602f7d",
    "docker_token_proof": "54e68a39d83c0e8dd716ca024ffcbd50f2a4749613a9d368ae36c4594fd7e513",
    "jenkins_docker_ps": "2acb65a93b0e1c7d9e9d7df4999d3f7dcca49e0a932b85319a32bf17b304f7f3",
    "buildapp_console": "5867956c1098a0d2603ba188957c5ea6c8543ce924e11fb6da061fc15eaed7b8",
    "testapp_console": "bd0c7f7e0fe8070887a7e1045050c9c9d171382937f11c854dbd96f744d3c841",
    "pipeline_script": "6ddcb6d2a9c1bd545bda010eba0a2940cc978e496aed9c5f6b70b8d7f58bd971",
    "pipeline_console": "263bf77ada327684003c3f802ae975f2f3bb70e5e05c94f61abf8324bc90aafe",
    "jenkins_url": "d095fe147c37a69451d82eee12259e27d86848e206ae75a37c3de31c6a456aab",
    "ansible_ping": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "ansible_hello": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "ansible_playbook_install": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "ports_conf_after": "c41a881f6b628b5bc2771dfa6125eb0744f272b666aead54c09b20a8c766c72d",
    "curl_apache_8081": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "signup_v1": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "login_v1": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "signup_v2": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "login_v2": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "db_tables": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    "db_user_hash_sample": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
  },
  "validation_passed": false,
  "run": {
    "python": "3.8.2",
    "platform": "linux"
  }
}
```
```text
pytest -q

(.venv) devasc@labvm:~/devnet-day1-IB-23-5B-Suleimanov$ python -m pytest -q
....                                                                     [100%]
4 passed in 0.59s

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
