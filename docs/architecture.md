# OpenTaxAI Architecture

OpenTaxAI is currently a local-first tax calculation workflow with a legacy script entrypoint. The intended architecture is modular so tax rules, broker parsers, AI assistants, and MCP tools can evolve independently.

## Current Components

- `run.py`: legacy local workflow for reading broker exports and calculating capital gains.
- `tests/`: synthetic unit tests for parsing helpers, time windows, moving-average gains, and short selling.
- `.github/`: issue templates, pull request checklist, and CI.

## Target Components

- `opentaxai.parsers`: broker export readers and field mapping.
- `opentaxai.rules`: jurisdiction-specific tax rule interfaces.
- `opentaxai.calculators`: FIFO, moving average, and future cost basis engines.
- `opentaxai.reports`: CSV, Markdown, and human-reviewable calculation traces.
- `opentaxai.ai`: AI-assisted explanations, validation, and workflow guidance.
- `opentaxai.mcp`: local MCP server for tax automation tools.
- `opentaxai.agents`: import, validate, calculate, review, and report workflows.

## Privacy Model

OpenTaxAI should be local-first by default. Real trade records should not leave the user's machine unless the user explicitly configures an external service. Tests and issue reports should use synthetic or anonymized data only.
