# Documentation

## Project layout

The Django project uses a standard `src` layout. Application packages and
runtime assets live under `src/`, while `manage.py`, packaging metadata, and
dependency locks remain at the repository root.

Run commands from the repository root, or use `python bin/run.py <command>` to
invoke Django from another working directory. The root entrypoint adds `src/` to
Python's import path before loading `config.settings`.

## Validation

The supported local checks are:

```text
python manage.py check
python manage.py test
python -m compileall -q src manage.py bin
```

See the architecture decision record in `adr/0001-src-layout.md` for the
reasoning behind this structure.
