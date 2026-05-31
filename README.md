# OpenTaxAI

Open-source AI-native tax automation platform.

OpenTaxAI helps individuals and developers build transparent, programmable, and privacy-preserving tax workflows. The current implementation focuses on local capital gains calculation from brokerage trade records, with a roadmap toward AI-assisted tax automation, MCP integration, and agent-based workflows.

> Disclaimer: OpenTaxAI is not tax, legal, or investment advice. Tax rules vary by jurisdiction, residency, year, broker, and filing context. Always review outputs before filing or consult a qualified professional.

## Vision

OpenTaxAI aims to make tax workflows transparent, programmable, and accessible through AI-powered automation.

Tax preparation often depends on opaque spreadsheets, manual broker exports, and hard-to-review calculations. OpenTaxAI is designed to become open infrastructure for tax automation: local-first, auditable, extensible, and safe for sensitive financial data.

## Features

- Tax calculation workflows
- Local capital gains calculation from brokerage trade records
- FIFO and moving-average cost basis workflows
- Hong Kong stock, US stock, and multi-currency trade record support
- Privacy-first local execution for sensitive financial data
- AI-assisted tax automation (planned)
- MCP integration (planned)
- Agent-based workflows (planned)
- Open-source infrastructure for tax rule engines and filing assistants

## Current Capabilities

- Reads UTF-16, tab-separated brokerage order history exports.
- Filters failed and cancelled orders.
- Calculates realized gains and fees for a selected tax year.
- Supports buy, sell, and short-selling close workflows.
- Produces per-symbol and portfolio-level summaries.
- Includes unit tests that use synthetic data only.

## Quick Start

OpenTaxAI currently requires Python 3.9 or higher and has no third-party runtime dependencies.

```bash
python3 run.py
```

The legacy script expects local broker exports at:

```text
data/订单历史-综合账户.csv
data/订单历史-港股融资融券.csv
data/订单历史-美股融资融券.csv
```

These files usually contain personal financial information. The repository ignores `*.csv`; do not commit real trade records.

## Tax Year

Update the tax-year window in `run.py`:

```python
start_time = "20250101"
end_time = "20251231"
```

## Cost Basis Method

The current workflow defaults to moving average:

```python
tax_data = MA(code_data, start_time, end_time)
```

To use FIFO:

```python
tax_data = FIFO(code_data, start_time, end_time)
```

## Development

Run tests:

```bash
python3 -m unittest discover
```

The test suite uses synthetic transactions only. It does not read broker CSV files.

## Architecture

See [docs/architecture.md](docs/architecture.md) for the current architecture and planned migration from a legacy script to modular OpenTaxAI components.

## Roadmap

- [x] Initial architecture
- [x] Local capital gains calculation workflow
- [x] Synthetic unit tests and GitHub Actions CI
- [ ] Tax rule engine
- [ ] AI tax assistant
- [ ] MCP server support
- [ ] Agent-based workflow runner
- [ ] Multi-country tax support
- [ ] Automated testing for broker import formats
- [ ] Report export for human review

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md). Tax logic changes must include jurisdiction, tax year, method, references, anonymized samples, and tests.

## Security and Privacy

Do not upload real trade records, account names, order IDs, screenshots, or broker statements to issues or pull requests. Security concerns should follow [SECURITY.md](SECURITY.md).

## License

MIT License. See [LICENSE](LICENSE).
