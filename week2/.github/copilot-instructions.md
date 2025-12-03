**Repository Overview**
- **Language:**: Primary artifacts are simple Python scripts (example: `Activity 3.py`).
- **Purpose:**: Course exercises / small activities — expect single-file scripts and small folders named `Activity 1`, `Activity 2`.

**What to change**
- **Keep file-level structure**: Do not convert these exercises into packages without confirmation — these are coursework scripts.
- **Preserve function names**: Example functions in `Activity 3.py` such as `fib_series` and `factorial` are referenced by the runner; keep signatures unless you update call-sites.

**How to run locally (Windows PowerShell)**
- **Run script:**: `python "Activity 3.py"` (quotes required because workspace paths and filenames may contain spaces).

**Typical patterns discovered**
- **Input-driven scripts:**: Scripts prompt via `input()` (see `Activity 3.py`) and print results directly. When modifying, keep CLI prompts simple and stable.
- **No dependency files found:**: There is no `requirements.txt` or `pyproject.toml` present — treat the code as plain Python 3 scripts.

**Agent guidance (concise, actionable)**
- **Edit scope:**: Make minimal, focused edits to the existing script files. Example: improve `factorial` to return `None` for negative inputs (already present) or add docstrings.
- **Testing approach:**: Use direct runs of the script for verification. For `Activity 3.py` a quick check is to run with small integers (e.g., `3`) and validate printed output.
- **Naming / quoting:**: Files/folders have spaces (e.g., `Activity 1`) — always show examples with quoted paths in PowerShell.

**When merging or updating this file**
- **If a previous `.github/copilot-instructions.md` exists:**: Preserve any repository-specific policies already present. Merge only actionable, code-discoverable items — do not add speculative processes.

**Key files to inspect for context**
- `Activity 3.py` — example script showing `fib_series` and `factorial` functions and CLI input usage.
- `Activity 1/`, `Activity 2/` — directories likely containing other exercise files; inspect before refactoring.

**Ask the user before**
- Converting scripts to packages or adding dependency management files.
- Changing CLI behavior (argument parsing, I/O) that could break grading/test harnesses.

If anything here is unclear or you'd like me to include additional examples (unit-test snippets, a `requirements.txt` proposal, or CI hints), tell me which direction and I will iterate.
