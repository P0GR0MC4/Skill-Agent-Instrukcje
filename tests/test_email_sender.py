from unittest.mock import patch, MagicMock
from mailer.email_sender import EmailSender


@patch('smtplib.SMTP')
def test_send_success(mock_smtp):
    instance = mock_smtp.return_value.__enter__.return_value
    instance.sendmail = MagicMock()

    sender = EmailSender(smtp_host='localhost', smtp_port=1025)
    result = sender.send('user@example.com', 'Hi', 'Body')

    assert result['success'] is True
    instance.sendmail.assert_called()


@patch('smtplib.SMTP')
def test_send_failure(mock_smtp):
    instance = mock_smtp.return_value.__enter__.return_value
    instance.sendmail.side_effect = Exception('fail')

    sender = EmailSender(smtp_host='localhost', smtp_port=1025)
    result = sender.send('user@example.com', 'Hi', 'Body')

    assert result['success'] is False
    assert 'fail' in result['error']
