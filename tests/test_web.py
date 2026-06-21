import pytest
from unittest.mock import patch
from mailer.web import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


@patch("mailer.web.render_template")
def test_index_get(mock_render, client):
    mock_render.return_value = "mocked html"
    response = client.get("/")
    assert response.status_code == 200
    mock_render.assert_called_once()


@patch("mailer.web.render_template")
def test_subscribe_valid_email(mock_render, client):
    mock_render.return_value = "mocked html"
    response = client.post("/subscribe", data={"email": "test@example.com"})
    assert response.status_code in [200, 302]


@patch("mailer.web.render_template")
def test_subscribe_invalid_email(mock_render, client):
    mock_render.return_value = "mocked html"
    response = client.post("/subscribe", data={"email": "invalid-email"})
    assert response.status_code in [200]
    mock_render.assert_called()


@patch("mailer.web.email_sender.send")
@patch("mailer.web.render_template")
def test_send_valid_recipient(mock_render, mock_send, client):
    mock_render.return_value = "mocked html"
    mock_send.return_value = {"success": True, "error": None}
    response = client.post(
        "/send",
        data={
            "recipient": "test@example.com",
            "subject": "Test",
            "body": "Test body",
        },
    )
    assert response.status_code in [200, 302]


@patch("mailer.web.render_template")
def test_send_invalid_recipient(mock_render, client):
    mock_render.return_value = "mocked html"
    response = client.post(
        "/send",
        data={
            "recipient": "invalid",
            "subject": "Test",
            "body": "Test body",
        },
    )
    assert response.status_code == 200
    mock_render.assert_called()
