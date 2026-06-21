from flask import Flask, render_template, request, redirect, url_for
from mailer.subscribers import SubscriberManager
from mailer.validators import EmailValidator
from mailer.email_sender import EmailSender

app = Flask(__name__)
subscriber_manager = SubscriberManager()
email_sender = EmailSender()


@app.route("/", methods=["GET"])
def index():
    subscribers = subscriber_manager.list()
    return render_template(
        "welcome.html",
        user_name="Użytkowniku",
        confirmation_url=url_for("index", _external=True),
        subscribers=subscribers,
    )


@app.route("/subscribe", methods=["POST"])
def subscribe():
    email = request.form.get("email", "").strip()
    if not EmailValidator.validate(email):
        return render_template(
            "welcome.html",
            user_name="Użytkowniku",
            confirmation_url=url_for("index", _external=True),
            subscribers=subscriber_manager.list(),
            error="Nieprawidłowy adres e-mail.",
        )

    subscriber_manager.add(email)
    return redirect(url_for("index"))


@app.route("/send", methods=["POST"])
def send_email():
    recipient = request.form.get("recipient", "").strip()
    subject = request.form.get("subject", "Mailer Notification")
    body = request.form.get("body", "Hello from Mailer.")

    if not EmailValidator.validate(recipient):
        return render_template(
            "welcome.html",
            user_name="Użytkowniku",
            confirmation_url=url_for("index", _external=True),
            subscribers=subscriber_manager.list(),
            error="Nieprawidłowy adres odbiorcy.",
        )

    result = email_sender.send(recipient, subject, body)
    if not result["success"]:
        return render_template(
            "welcome.html",
            user_name="Użytkowniku",
            confirmation_url=url_for("index", _external=True),
            subscribers=subscriber_manager.list(),
            error=f"Błąd wysyłki: {result['error']}",
        )

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
