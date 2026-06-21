# GitHub Copilot Instructions - Mailer Project

## 1. Globalne Standardy Technologiczne
* **Python i Zależności:** Python 3.9+, ścisłe przestrzeganie PEP 8. Formatowanie kodu za pomocą `black` i sprawdzanie przez `flake8`.
* **Typowanie:** Typowanie (Type hints) jest obowiązkowe dla wszystkich funkcji i metod.
* **Zależności:** Każda nowa biblioteka musi trafić do `requirements.txt`.

## 2. Architektura i Struktura Kodu
* **Rozmiar plików:** Moduły (pliki `.py`) mogą mieć maksymalnie 500 linii kodu.
* **Rozmiar funkcji:** Funkcje i metody mogą mieć maksymalnie 50 linii kodu.
* **Zasada SOLID:** Klasy muszą odpowiadać za jedną, konkretną odpowiedzialność (Single Responsibility Principle).

## 3. Wytyczne dla Komponentów Projektu

### mailer/ (Logika Biznesowa)
* Wszystkie serwisy, integracje z API pocztowymi oraz obsługa baz danych znajdują się tutaj.
* **Obsługa błędów:** Każda operacja I/O (wysyłka maila, zapis do bazy) musi być otoczona blokiem `try-except` z dedykowanym logowaniem błędów. Nie wyciszaj błędów (no bare `except:`).

### templates/ (Flask HTML)
* Szablony HTML dla frameworka Flask (Jinja2).
* Struktura musi być modularna (używaj `{% extends %}` oraz `{% include %}`).
* Wszystkie zmiennes przekazywane do szablonów muszą być bezpiecznie renderowane.

### static/ (CSS / JavaScript)
* **JavaScript:** Czysty JS (Vanilla JS) lub zgodny z konfiguracją projektu. Kod pisany w trybie `'use strict';`.
* **CSS:** Klasy nazywane według czytelnego klucza (np. BEM lub standardowe, jasne nazwy powiązane z komponentami).

### tests/ (Testy automatyczne)
* Używamy frameworka `pytest` oraz wtyczki `pytest-cov`.
* **Wymóg:** Minimum 80% pokrycia kodu testami (code coverage).
* **Izolacja:** Całkowity zakaz wysyłania prawdziwych wiadomości e-mail oraz odpytywania produkcyjnych baz danych podczas testów. Obowiązkowe stosowanie mocków (`unittest.mock` lub fixturek pytest).

## 4. Testing Strategy (Integracja ze Skillami)
Zwróć się do "Mailer Complete Testing Skill" dla szczegółów implementacyjnych.

Minimum requirements:
- Każda funkcja: min. 2 testy
- Edge cases + error handling
- Mocking external services
- Coverage: min. 80%

Polecenie kontekstowe: "Use mailer-complete-testing skill"

## 5. Bezpieczeństwo
* **Sekrety:** Całkowity zakaz umieszczania haseł, kluczy API (np. do SendGrida/Mailguna) i tokenów w kodzie.
* **Konfiguracja:** Wszystkie wrażliwe dane muszą być pobierane z zmiennych środowiskowych (`os.environ` lub `python-dotenv`).
* **Walidacja:** Obowiązkowa walidacja każdego adresu e-mail na wejściu (regex / biblioteki walidacyjne).
* **Baza danych:** Ochrona przed SQL Injection poprzez stosowanie ORM (np. SQLAlchemy) lub parametryzowanych zapytań.

## 6. Praca z Gitem i Zarządzanie Kodem
* **Konwencja commitów:** Stosuj *Conventional Commits* (np. `feat: add email validation`, `fix: resolve smtp timeout`, `docs: update readme`).
* **Nazewnictwo gałęzi (Branches):**
    * Nowe funkcje: `feature/nazwa-zadania`
    * Poprawki błędów: `bugfix/nazwa-bledu`
    * Dokumentacja: `docs/nazwa-zmiany`
* **Pull Requests (PRs):** Każdy PR musi zawierać opis zmian oraz powiązane testy jednostkowe.