# Storage Load Tester

A simple Python-based storage workload generator and benchmark tool.

## What the tool does

- Executes a set of pre-defined OLTP and streaming workloads.
- Measures performance metrics such as throughput, latency, and errors.
- Produces JSON results for easy analysis and reporting.
- Designed for automation and repeatable load testing.

## How to run it

From the repository root:

```bash
python run_tests.py
```

If you want to run individual workload modules, inspect `src/` scripts:
- `src/runner.py` — orchestrates test execution
- `src/workloads.py` — contains workload definitions
- `src/parser.py` — parses args and test configs
- `src/report.py` — generates final output

## Example workloads

This repository contains workloads in the root:
- `oltp.0.0`, `oltp.1.0`, `oltp.2.0`, `oltp.3.0`
- `stream.0.0` through `stream.7.0`

Each workload file is a test scenario. `run_tests.py` runs all available workloads by default.

## Example output

After running tests, results are saved under:
- `results/oltp.json`
- `results/stream.json`

Output format (example):

```json
{
  "workload": "oltp.0.0",
  "throughput": 12345,
  "latency_ms": {
    "p50": 5.6,
    "p95": 12.3,
    "p99": 27.8
  },
  "errors": 0
}
```

## Quick usage

```bash
python run_tests.py
```
