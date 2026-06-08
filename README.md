
# data.aykhan.net - Static Data API

<div align="center">
  <img src="https://media.aykhan.net/assets/logos/aykhannet.ico" alt="Aykhan.net Logo">
</div>

Welcome to my GitHub repository "data.aykhan.net"! This repository serves as an API for static data, providing essential resources for various projects and tasks. Here, you'll find structured data and endpoints to access it.

## API Usage

You can access the static data through this API by making HTTP requests to specific endpoints. Here are some of the available endpoints:

- `https://data.aykhan.net/data/general/movies.json`: Get information about movies.
- `https://data.aykhan.net/data/general/users.json`: Retrieve user details.
- `https://data.aykhan.net/data/general/theatres.json`: Access event information.

Feel free to explore and utilize this data for your projects.

## Public data index (`data-index.json`)

`generate_index.py` produces two public, read-only metadata files consumed by the
[Aykhan Terminal Gateway](https://aykhan.net/terminal):

- **`data-index.json`** — every indexed JSON endpoint (`name`, `path`, `url`,
  `sizeBytes`) and `totalEndpoints`.
- **`build-report.json`** — `service`, `generatedAt`, `totalEndpoints`,
  `indexedFolders`, `skippedFolders`, and `notes`.

Run it from the repo root (it also refreshes the browsable `index.html` listings):

```
python generate_index.py
```

### Which endpoints are indexed

Indexing is **whitelist-based**. Only these top-level folders are scanned:

```
data · public
```

…and only `.json` files within them are indexed.

### Security note — public metadata only

The index publishes only **metadata** (`name`/`path`/`url`/`sizeBytes`); it never
inlines file contents. It **excludes** hidden/dotfiles, `.env`, secrets, and
anything under `private`/`drafts`/`secrets`/`node_modules`. The whitelist is
opt-in, so a new folder is *not* indexed until it is explicitly added. All listed
endpoints are already public static files (the sample datasets such as
`users.json` contain synthetic placeholder data, not real personal information).

## Website

While this repository primarily serves as a data API, you can visit [aykhan.net](https://aykhan.net) to explore my portfolio and interactive web development projects.

## Contribution

I welcome contributions and feedback from the developer community. If you find any issues, have suggestions, or wish to contribute to the API, feel free to:

- Open an issue
- Create a pull request

Your contributions are highly appreciated as they help improve the quality of this repository.

## Technologies Used

- JSON: A lightweight data interchange format used for structuring data.

## License

This repository is licensed under the [MIT License](LICENSE). You are free to use the code, modify it, and distribute it under the terms of the license.

Let's connect and collaborate!
