# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code)
when working with code in this repository.

## Project Overview

**validate-docbr** is a Python package for validating and
generating Brazilian documents (CPF, CNPJ, CNH, CNS, PIS,
Título Eleitoral, RENAVAM, Certidão). Published on PyPI as
`validate-docbr`, version **2.0.1**.

## Language Conventions

- **Code** (class names, method names, variables): **English**
- **Comments, docstrings, docs, commits, issues**: **pt-BR**
- **Claude files** (CLAUDE.md, agents, commands): **English**

## Tooling

- **Package manager**: [uv](https://docs.astral.sh/uv/)
  (`pyproject.toml` + `uv.lock`)
- **Type checker**: [ty](https://docs.astral.sh/ty/)
- **Task runner**: [Task](https://taskfile.dev/)
  (`Taskfile.yml`)
- **Tests**: pytest 9.0.2 + pytest-cov 7.1.0
- **Python**: >= 3.10 (tested 3.10–3.14)

## Commands

```bash
task build            # Build Docker image (installs git hooks)
task test             # Run all tests with pytest
task test-coverage    # Run tests with coverage (threshold 98%)
task type-check       # Run ty type checker
task lint             # Run all linters
task lint-fix         # Auto-fix Python lint issues
task ci               # Run lint + test-coverage
task shell            # Open a bash shell in the container
```

To run a single test:

```bash
uv run pytest tests/test_CPF.py
uv run pytest tests/test_CPF.py::TestCpf::test_mask
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
5. Run `task type-check` and `task test-coverage`

## Coding Conventions

- **Type hints**: modern generic syntax
  (`list[str]`, `str | None`) — no `typing` imports (PEP 585)
- **Imports**: absolute style
  (`from validate_docbr.DocumentBase import DocumentBase`)
- **Tests**: Given-When-Then with `# Given`, `# When`,
  `# Then` comments
- **Type safety**: code must pass `ty check` with no errors

## CI/Pre-push

- **Pre-push hook** runs lint + test-coverage
  (installed via `task build`)
- **GitHub Actions** (`ci.yml`) runs lint then tests
  across Python 3.10–3.14 using `uv`
- Coverage must stay at or above **98.00%**
