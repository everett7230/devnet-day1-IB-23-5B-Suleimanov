#!/usr/bin/env python3
import hashlib
import json
import os
from pathlib import Path

import requests

BASE = "https://webexapis.com/v1"
ART = Path("artifacts/day5/webex")


def token_hash8(token: str) -> str:
    return hashlib.sha256(token.encode("utf-8")).hexdigest()[:8]


def save_json(path: Path, data) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8"
    )


def main() -> int:
    webex_token = os.getenv("WEBEX_TOKEN", "").strip()
    student_token = os.getenv("STUDENT_TOKEN", "").strip()

    if not webex_token:
        raise SystemExit("WEBEX_TOKEN is not set")
    if not student_token:
        raise SystemExit("STUDENT_TOKEN is not set")

    th8 = token_hash8(student_token)
    room_title = f"Day5-Room-{th8}"
    message_text = f"Day5 message TOKEN_HASH8={th8}"

    headers = {
        "Authorization": f"Bearer {webex_token}",
        "Content-Type": "application/json",
    }

    me = requests.get(f"{BASE}/people/me", headers=headers, timeout=30)
    me.raise_for_status()
    save_json(ART / "me.json", me.json())

    rooms = requests.get(f"{BASE}/rooms", headers=headers, timeout=30)
    rooms.raise_for_status()
    save_json(ART / "rooms_list.json", rooms.json())

    room_create = requests.post(
        f"{BASE}/rooms",
        headers=headers,
        json={"title": room_title},
        timeout=30,
    )
    room_create.raise_for_status()
    room_data = room_create.json()
    save_json(ART / "room_create.json", room_data)

    room_id = room_data["id"]

    msg_post = requests.post(
        f"{BASE}/messages",
        headers=headers,
        json={"roomId": room_id, "text": message_text},
        timeout=30,
    )
    msg_post.raise_for_status()
    save_json(ART / "message_post.json", msg_post.json())

    msgs = requests.get(
        f"{BASE}/messages",
        headers=headers,
        params={"roomId": room_id, "max": 10},
        timeout=30,
    )
    msgs.raise_for_status()
    save_json(ART / "messages_list.json", msgs.json())

    print(f"Webex artifacts created for TOKEN_HASH8={th8}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
