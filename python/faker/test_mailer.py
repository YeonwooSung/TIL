from unittest.mock import patch

import pytest

import smtplib
import email.message
from faker import Faker


def send(sender, to, subject="None", body="None", server="localhost"):
    """메시지를 전송한다."""
    message = email.message.Message()
    message["To"] = to
    message["From"] = sender
    message["Subject"] = subject
    message.set_payload(body)

    client = smtplib.SMTP(server)
    try:
        return client.sendmail(sender, to, message.as_string())
    finally:
        client.quit()



@pytest.mark.parametrize("iteration", range(10))
def test_send(faker: Faker, iteration: int):
    sender = faker.email()
    to = faker.email()
    body = faker.paragraph()
    subject = faker.sentence()

    with patch("smtplib.SMTP") as mock:
        client = mock.return_value
        client.sendmail.return_value = {}

        res = send(sender, to, subject, body)

        assert client.sendmail.called
        assert client.sendmail.call_args[0][0] == sender
        assert client.sendmail.call_args[0][1] == to
        assert subject in client.sendmail.call_args[0][2]
        assert body in client.sendmail.call_args[0][2]
        assert res == {}
