# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code)
when working with code in this repository.

## Project Overview

**validate-docbr** is a Python package for validating and
generating Brazilian documents (CPF, CNPJ, CNH, CNS, PIS,
Título Eleitoral, RENAVAM, Certidão). Published on PyPI as
`validate-docbr`. Currently working toward **v2.0.0**
(see issue #67).

## Language Conventions

- **Code** (class names, method names, variables): **English**
- **Comments, docstrings, docs, commits, issues**: **pt-BR**
- **Claude files** (CLAUDE.md, agents, commands): **English**

## Commands

All commands run via Docker using [Task](https://taskfile.dev/).
Run `task build` first to set up the container.

```bash
task build            # Build Docker image (installs git hooks)
task test             # Run all tests with pytest
task test-coverage    # Run tests with coverage (threshold 98%)
task lint             # Run all linters
task lint-fix         # Auto-fix Python lint issues
task shell            # Open a bash shell in the container
```

To run a single test file or test inside the container:

```bash
docker compose run --rm -v $(pwd):/app app \
  pytest tests/test_CPF.py
docker compose run --rm -v $(pwd):/app app \
  pytest tests/test_CPF.py::TestCpf::test_mask
```

## Architecture

Every document type is a class inheriting from `DocumentBase`
(ABC in `validate_docbr/DocumentBase.py`).
`DocumentBase` defines the interface:

- `validate(doc)` — abstract, validates a document string
- `generate(mask)` — abstract, generates a valid document
- `mask(doc)` — abstract, applies formatting mask
- `validate_list`, `generate_list` — concrete methods
- `_only_digits`, `_validate_input` — shared utilities

Unimplemented abstract methods raise
`FunctionNotImplementedError`
(defined in `validate_docbr/exceptions.py`).

Each document class (e.g., `CPF.py`, `CNPJ.py`) implements
the three abstract methods with document-specific validation
logic (check digits, length, masks). Imports use absolute
style: `from validate_docbr.DocumentBase import DocumentBase`.

`generic.py` provides `validate_docs()`, a standalone function
that validates heterogeneous document lists.

## Adding a New Document

1. Create a class in `validate_docbr/` inheriting from
   `DocumentBase`, named by the document's acronym
2. Implement `validate`, `generate`, and `mask`
3. Export it in `validate_docbr/__init__.py`
4. Add tests in `tests/test_<Name>.py`
   (use `unittest` with Given-When-Then pattern)

## Coding Conventions

- **Type hints**: modern generic syntax
  (`list[str]`, `str | None`) — no `typing` imports (PEP 585)
- **Imports**: absolute style
  (`from validate_docbr.DocumentBase import DocumentBase`)
- **Tests**: Given-When-Then with `# Given`, `# When`,
  `# Then` comments

## CI/Pre-push

- **Pre-push hook** runs lint + test-coverage
  (installed via `task build`)
- **GitHub Actions** (`ci.yml`) runs lint then tests
  on PRs to `main`
- Coverage must stay at or above **98.00%**

## v2.0.0 Roadmap (issue #67)

- [x] Rename `BaseDoc` → `DocumentBase`
- [x] Abstract methods raise `FunctionNotImplementedError`
- [x] Type hints modernized to PEP 585 generic syntax
- [x] Tests refactored to Given-When-Then pattern
- [x] Coverage threshold raised to 98%
- [x] Accept new alphanumeric CNPJ format
- [x] Improve code readability
- [x] Use RegEx for document string validation
- [x] Improve docstrings (Google Style Guide)
- [x] Migrate Makefile to Taskfile
- [x] Migrate documentation tool (MkDocs to Docsify)
