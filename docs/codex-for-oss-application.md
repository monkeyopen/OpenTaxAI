# Codex for Open Source Application Draft

## Project

OpenTaxAI is an open-source AI-native tax automation platform. It starts with local capital gains calculation from brokerage trade records and is designed to grow into programmable infrastructure for tax rule engines, AI tax assistants, MCP integrations, and agent-based tax workflows.

## Why this project matters

Tax workflows are often manual, spreadsheet-heavy, and difficult to audit. Individual investors also handle sensitive financial data that should not be uploaded to closed services without a clear reason. OpenTaxAI provides a local-first and transparent alternative: users can inspect the calculation logic, run it on their own machine, and contribute anonymized test cases for broker formats and tax-rule behavior.

The current repository includes a working local capital gains workflow, MIT License, contribution guidelines, security policy, roadmap, GitHub issue/PR templates, CI, and synthetic unit tests.

## How Codex/API credits would be used

API credits would support core open-source maintenance:

- Review PRs that modify tax calculation behavior.
- Check issues and PRs for accidental disclosure of real trade records.
- Generate regression tests from anonymized broker samples.
- Draft parser mappings for new broker export formats.
- Explain calculation traces in human-readable reports.
- Build and test an MCP server for local tax workflows.
- Prototype agent-based workflows for import, validation, calculation, and report generation.

All automation should use public code and anonymized examples only. Real user trade records should stay local.

## Repository description

Open-source AI-native tax automation platform.

## Suggested topics

`ai`, `tax`, `automation`, `agent`, `mcp`, `open-source`, `python`, `fintech`
