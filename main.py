from __future__ import annotations
from json import JSONDecodeError

from http.client import HTTPConnection, HTTPSConnection
import json


def lima(payload: str, lang: str = "eng", conn: str | HTTPConnection = None) -> str:
    if isinstance(conn, str):
        conn = HTTPSConnection(conn)

    conn.request("POST", f"/?lang=ud-{lang}&pipeline=deepud", payload)

    res = conn.getresponse()
    data = res.read().decode("utf-8")

    try:
        return json.loads(data)["tokens"]
    except JSONDecodeError as e:
        print(data)
        raise e


if __name__ == "__main__":
    conn = HTTPSConnection("www.example.com")  # A CHANGER POUR SE CONNECTER AU SERVEUR LIMA
    payload = "また金曜日に".encode("utf-8")

    lang = "fra"

    res = lima(conn=conn, payload=payload, lang=lang)

    print(res)
