# Mailer — Konfiguracja Copilot, Skills i Agenci

Repozytorium zawiera konfiguracje i zasoby wspierające pracę z projektem Mailer oraz przykładowe Skills i Agenci dla GitHub Copilot.

**Struktura i ważne pliki:**

- [copilot-instructions.md](copilot-instructions.md) — globalne wytyczne projektu (wersja Pythona, PEP8, testy, bezpieczeństwo).
- [.copilot/](.copilot/) — definicje Skills (email-validation, mailer-testing, email-templates).
- [.agents/](.agents/) — konfiguracje Agentów (docs-generator-agent).
- [templates/](templates/) — szablony e-mail (HTML i TXT), w tym `base_email.html`.
- [mailer/](mailer/) — moduły aplikacji (przykładowo: `email_sender.py`, `subscribers.py`, `validators.py`).
- [static/](static/) — zasoby statyczne (CSS, JS).
- [tests/](tests/) — testy jednostkowe (pytest).
- [requirements.txt](requirements.txt) — zależności Pythona.

Jak uruchomić projekt (lokalnie):

1. Utwórz i aktywuj środowisko wirtualne (opcjonalnie):

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Unix/macOS
source .venv/bin/activate
```

2. Zainstaluj zależności:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

3. Uruchom testy i raport coverage:

```bash
python -m pytest --cov=mailer
```

Lintery i formatowanie:

- Formatowanie: `black .`
- Statyczna analiza: `flake8 .` / `mypy .` (jeśli skonfigurowane)

Korzystanie z Skills i Agentów:

- Przed implementacją zapoznaj się z `copilot-instructions.md`.
- Użyj Skill, np. `@copilot use email-validation`, aby generować wzorce kodu i testów.
- Aby wygenerować dokumentację, użyj agenta skonfigurowanego w `.agents/docs-generator-agent.yaml` (trigger: "Generate documentation for [module]").