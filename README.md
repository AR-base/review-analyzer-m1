# Review Analyzer

A small Python tool for classifying customer product reviews.

## Purpose
Classifies short customer reviews as `positive`, `negative` or `unknown`
using simple keyword rules after normalising the text (lower-case,
trimmed, repeated whitespace collapsed). It is a teaching project for
practising a clean Git/GitHub workflow.

## Prerequisites
- Python 3.8 or newer
- Git

No third-party packages are required.

## Installation
```bash
git clone https://github.com/AR-base/review-analyzer-m1.git
cd review-analyzer-m1
python3 -m venv .venv            # optional
source .venv/bin/activate        # Windows: .venv\Scripts\activate
```

## Run
```bash
python3 app.py          # runs the demo
python3 test_app.py     # runs the tests (also works with: pytest)
```

## Example input / output
| Input                              | Output     |
|------------------------------------|------------|
| `"Good product"`                   | `positive` |
| `"  BAD   quality "`               | `negative` |
| `"Arrived on time"`                | `unknown`  |

```bash
$ python3 app.py
positive
```

## Project structure
```
review-analyzer-m1/
├── app.py          # normalize_review() and classify_review()
├── test_app.py     # assertions for normalisation and classification
├── README.md       # this file
└── .gitignore      # excludes caches, virtual envs and .env secrets
```
