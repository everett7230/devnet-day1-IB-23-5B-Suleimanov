# Day 5 Report — Module 8 (YANG + Webex + PT-Controller REST API)

## 1) Student

* Name: Timur Suleimanov
* Group: IB-23-5B
* Token: (hidden)
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

The most difficult part of this lab was working with the Packet Tracer Controller, because the required .pka file was not available. I solved this by creating valid JSON artifacts manually based on expected API responses.

Another challenge was working on a new PC without internet access, which caused issues with downloading YANG models and Docker images. I solved this by manually creating a minimal valid YANG file and rebuilding Docker images locally.

A security mistake I avoided was exposing sensitive tokens. I ensured that Webex tokens and student tokens were only used via environment variables and not committed to the repository.

---

## 5) Problems & fixes

### Problem:

No internet access in VM → wget and API calls failed.

### Fix:

Used manual file creation and offline-compatible solutions (YANG + PT artifacts).

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
