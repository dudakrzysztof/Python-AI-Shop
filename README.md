# Python-AI-Shop

## Django Shop

A small, typed Django 6.1 shop with product, customer, order, and newsletter apps.

## Setup

Run the commands from the repository root. Python 3.14+ is required. Install
dependencies with `python -m pip install -e .`, then run `python manage.py
migrate`, `python manage.py seed_demo`, and `python manage.py runserver`.

Set `SECRET_KEY`, `DEBUG`, and `ALLOWED_HOSTS` in deployment environments. SQLite
is the default database. `DATABASE_URL` supports sqlite, postgres/postgresql, and
mysql URLs through the standard-library parser (install a matching DB driver for
non-SQLite databases).

The UI uses the current stable HTMX 2.0.4 release from its official CDN and
standards-compatible modern CSS; it does not claim unsupported “HTMX4” or “CSS5”.
The JSON API is available at `/api/`. Payments use a `PaymentProvider` protocol
and deterministic manual provider suitable for development and tests.

Use `python manage.py check` and `python manage.py test` for built-in validation.
The same management commands can be run from any working directory with
`python bin/run.py check` or `python bin/run.py test`.

## Usage

The source layout is available directly from the repository root:

```pycon
>>> from pathlib import Path
>>> Path("src/config/settings.py").is_file()
True
>>> Path("src/templates/base.html").is_file()
True
```

## Repository map

- `src/config/` contains Django settings, URL routing, API wiring, and WSGI setup.
- `src/customer/`, `src/product/`, `src/order/`, and `src/newsletter/` contain the
  Django applications, migrations, views, forms, and API modules.
- `src/templates/` and `src/static/` contain the HTML templates and CSS assets.
- `manage.py` is the root management entrypoint; `bin/run.py` is a standard-library
  wrapper that runs it from any working directory.
- `docs/` contains project documentation and `adr/` contains architecture decisions.
- `backup/.gitkeep` reserves an empty backup directory for local operational use.
- `pyproject.toml` defines the package metadata and `uv.lock` pins dependency
  resolution. IDE configuration remains in `.idea/` at the repository root.