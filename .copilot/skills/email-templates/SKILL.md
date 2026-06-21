# Email Templates Skill

## Cel umiejętności
Wspieranie programistów w projektowaniu, dziedziczeniu, bezpiecznym podstawianiu zmiennych oraz testowaniu szablonów e-mail. Skill wymusza jednoczesne generowanie wersji HTML oraz Plain Text w celu zapewnienia wysokiej dostarczalności wiadomości i zapobieganiu wpadaniu do spamu.

## Wytyczne Architektoniczne i Reguły

### 1. Template Inheritance (Dziedziczenie)
Wszystkie szablony HTML muszą dziedziczyć z centralnego szablonu bazowego (`base_email.html`). Szablon bazowy definiuje globalną strukturę tabelaryczną (responsywność opartą na tabelach), style CSS wpisane bezpośrednio w tagi (inline styles) oraz sekcje blokowe dla zawartości i stopki.

### 2. Variable Substitution (Podstawianie Zmiennych)
- Wszystkie zmienne wstrzykiwane do szablonów Jinja2 muszą być jawnie typowane w warstwie Pythona.
- Wymagane jest stosowanie bezpiecznych wartości domyślnych przy użyciu filtra `| default`.
- Dane wrażliwe użytkowników (np. tokeny resetu hasła) muszą być przekazywane w sposób uniemożliwiający wyciek danych.

### 3. Dual Format Requirement
Dla każdego typu wiadomości e-mail deweloper ma obowiązek przygotować dwa pliki:
- Wersję `.html` – zawierającą ostylowaną strukturę wizualną.
- Wersję `.txt` – zawierającą surowy tekst z wyraźnie wydzielonymi sekcjami za pomocą znaków nowej linii, przeznaczoną dla klientów pocztowych bez obsługi HTML.

---

## Wzorce Kodowe (Code Examples)

### 1. Szablon Bazowy (`templates/base_email.html`)
```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{% block title %}Mailer Notification{% endblock %}</title>
</head>
<body style="margin: 0; padding: 0; font-family: Arial, sans-serif; background-color: #f4f4f4;">
    <table border="0" cellpadding="0" cellspacing="0" width="100%">
        <tr>
            <td style="padding: 20px 0 30px 0;">
                <table align="center" border="0" cellpadding="0" cellspacing="0" width="600" style="border-collapse: collapse; background-color: #ffffff; border: 1px solid #cccccc;">
                    <tr>
                        <td style="padding: 40px 30px 40px 30px;">
                            {% block content %}{% endblock %}
                        </td>
                    </tr>
                    <tr>
                        <td style="background-color: #333333; padding: 20px 30px 20px 30px; color: #ffffff; font-size: 12px; text-align: center;">
                            {% block footer %}&copy; 2026 Mailer Project. Wszelkie prawa zastrzeżone.{% endblock %}
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</body>
</html>
```