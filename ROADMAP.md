# OpenTaxAI Roadmap

## Done

- [x] Initial architecture
- [x] Local capital gains calculation workflow
- [x] FIFO and moving-average calculation support
- [x] Synthetic unit tests
- [x] GitHub Actions CI
- [x] Open-source governance docs

## Near Term

- [ ] Command-line options for tax year, exchange rate, and cost basis method
- [ ] Anonymized broker export samples
- [ ] Parser layer separated from calculation logic
- [ ] Tax rule engine interface
- [ ] Report export for human review
- [ ] More tests for short selling, stock splits, IPO allotments, and partial fills

## AI-Native Roadmap

- [ ] AI tax assistant for explaining calculations
- [ ] MCP server support for local tax workflows
- [ ] Agent-based workflows for importing, validating, calculating, and reporting
- [ ] Privacy checks for accidental sensitive-data disclosure in issues and PRs
- [ ] Multi-country tax workflow support

## Non-Goals

- OpenTaxAI does not store, upload, or synchronize user trade records.
- OpenTaxAI does not provide tax, legal, or investment advice.
- OpenTaxAI does not guarantee correctness for every jurisdiction, residency, broker, or filing scenario.
