<div align="center">

<img src="https://media.aykhan.net/assets/logos/aykhannet.ico" alt="aykhan.net logo" width="120" />

# data.aykhan.net

**A static, read‑only JSON "API" for the aykhan.net ecosystem — versioned data files served straight from GitHub Pages, with a whitelist‑generated endpoint index.**

[![Live](https://img.shields.io/badge/live-data.aykhan.net-235aa6?style=flat-square)](https://data.aykhan.net)
[![Index](https://img.shields.io/badge/index-data--index.json-1c1d25?style=flat-square)](https://data.aykhan.net/data-index.json)
[![Deploy](https://img.shields.io/badge/hosting-GitHub%20Pages-222?style=flat-square&logo=github)](https://pages.github.com)
[![Generator](https://img.shields.io/badge/generator-Python%203-f06449?style=flat-square&logo=python&logoColor=white)](./generate_index.py)
[![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)](./LICENSE)

</div>

---

## Overview

`data.aykhan.net` is a **static JSON API**: a collection of structured `.json` files served
directly over HTTPS from GitHub Pages, with no backend, database, or server runtime. Each
file is an endpoint, and a generated index describes the full surface — consumed by the
[Terminal Gateway](https://aykhan.net/terminal).

It is one of three independent, GitHub Pages–hosted repositories:

| Domain | Role |
| --- | --- |
| [aykhan.net](https://aykhan.net) | E‑portfolio + Terminal Gateway |
| [media.aykhan.net](https://media.aykhan.net) | Public media host + `media-index.json` |
| **[data.aykhan.net](https://data.aykhan.net)** | **Static JSON "API" + `data-index.json`** |

## Using the API

Every endpoint is a plain HTTP `GET` against a static URL:

```
https://data.aykhan.net/data/general/movies.json
https://data.aykhan.net/data/general/users.json
https://data.aykhan.net/data/general/theatres.json
```

```js
const movies = await fetch("https://data.aykhan.net/data/general/movies.json")
  .then((r) => r.json());
```

Browse the full, current list of endpoints in
[`data-index.json`](https://data.aykhan.net/data-index.json).

## The public index

[`generate_index.py`](./generate_index.py) produces two public, read‑only metadata files and
refreshes the browsable `index.html` listings:

| File | Contents |
| --- | --- |
| **`data-index.json`** | Every indexed endpoint — `name`, `path`, `url`, `sizeBytes` — plus `totalEndpoints`. |
| **`build-report.json`** | `service`, `generatedAt`, `totalEndpoints`, `indexedFolders`, `skippedFolders`, `notes`. |

```bash
python generate_index.py    # run from the repo root; no third-party dependencies
```

### What gets indexed

Indexing is **whitelist‑based** — a folder is invisible to the index until it is explicitly
allowed.

- **Scanned top‑level folders:** `data` · `public`
- **Allowed file type:** `.json` only

## Security model — public metadata only

This repository is **read‑only and public by design**. The index publishes **metadata
only** (`name` / `path` / `url` / `sizeBytes`); it never inlines file contents. The
generator excludes hidden/dotfiles, `.env`, secrets, and anything under
`private` / `drafts` / `secrets` / `node_modules`.

There are no tokens, API keys, secrets, uploads, or authentication anywhere in this system —
every published file is intended to be public.

## Project structure

```
data.aykhan.net/
├── data/                   # JSON endpoints (e.g. data/general/movies.json)
├── public/                 # Additional public JSON
├── generate_index.py       # Builds data-index.json + build-report.json + index.html
├── test_generate_index.py  # Generator tests
├── data-index.json         # Generated — public endpoint index
├── build-report.json       # Generated — build summary
├── index.html              # Generated — browsable listing
└── CNAME                   # data.aykhan.net
```

## License

Released under the [MIT License](./LICENSE) © 2023 Aykhan Ahmadzada.
