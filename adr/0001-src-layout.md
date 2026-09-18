# ADR 0001: Use a src layout

## Status

Accepted

## Context

The Django applications, templates, and static assets were previously placed
at the repository root. That layout made it easy for the working tree to be
imported accidentally and did not clearly separate source files from project
metadata, documentation, and operational directories.

## Decision

Keep `manage.py`, `pyproject.toml`, `uv.lock`, and IDE metadata at the
repository root, and place the Django project packages and runtime assets under
`src/`. The root management entrypoint adds `src/` to `sys.path`, so existing
commands such as `python manage.py check` continue to work without requiring a
shell-specific environment variable. `bin/run.py` provides the same behavior
when invoked outside the repository root.

## Consequences

Package discovery is explicitly configured with `src` as its package directory.
Settings resolve the project root independently from the `src/config` location,
while templates and static files are resolved under `src/`. Documentation lives
in `docs/`, architecture decisions live in `adr/`, and `backup/` is reserved
as an empty operational directory.
