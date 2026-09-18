# Python-AI-Shop
# Django Shop

A small, typed Django 6.1 shop with product, customer, order, and newsletter apps.

## Setup

Python 3.14+ is required. Install dependencies with `python -m pip install -e .`,
then run `python manage.py migrate`, `python manage.py seed_demo`, and
`python manage.py runserver`.

Set `SECRET_KEY`, `DEBUG`, and `ALLOWED_HOSTS` in deployment environments. SQLite
is the default database. `DATABASE_URL` supports sqlite, postgres/postgresql, and
mysql URLs through the standard-library parser (install a matching DB driver for
non-SQLite databases).

The UI uses the current stable HTMX 2.0.4 release from its official CDN and
standards-compatible modern CSS; it does not claim unsupported “HTMX4” or “CSS5”.
The JSON API is available at `/api/`. Payments use a `PaymentProvider` protocol
and deterministic manual provider suitable for development and tests.

Use `python manage.py check` and `python manage.py test` for built-in validation.