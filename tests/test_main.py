"""データベースを使わない設定（DB_HOST=none）で、画面と書き込みを確かめるテスト。"""

import os

os.environ.setdefault("DB_HOST", "none")
os.environ.setdefault("APP_TITLE", "テストの掲示板")
os.environ.setdefault("APP_VERSION", "9.9")

from fastapi.testclient import TestClient  # noqa: E402

from main import app  # noqa: E402

client = TestClient(app)


def test_トップページが開ける():
    res = client.get("/")
    assert res.status_code == 200
    assert "テストの掲示板" in res.text


def test_書き込むと一覧に出る():
    res = client.post("/", data={"text": "はじめまして"})
    assert res.status_code == 200
    assert "はじめまして" in res.text


def test_ヘルスチェック():
    assert client.get("/health").json() == {"status": "ok"}


def test_版とPodの名前が出る():
    import socket

    res = client.get("/")
    assert "hitokoto 9.9" in res.text
    assert socket.gethostname() in res.text
