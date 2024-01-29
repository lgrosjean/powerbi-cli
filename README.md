![PyPI - Version](https://img.shields.io/pypi/v/powerbi-cli?logo=pypi&color=blue&link=https%3A%2F%2Fpypi.org%2Fproject%2Fpowerbi-cli%2F)
![test](https://ghcr-badge.egpl.dev/lgrosjean/powerbi-cli/latest_tag?color=%2344cc11&ignore=latest&label=docker&trim=-)

# PowerBI CLI application


This applicaton is basically a Click wrapper around the [`pbipy`](https://github.com/andrewvillazon/pbipy) Python package, following the NodeJS CLI application [`powerbi-cli`](https://github.com/powerbi-cli/powerbi-cli) convention and documentation.

Its main feature is the Docker image available in parallel which can be used for various task like:
- Frequently export PowerBI Report `pbix` from PowerBI Service for historization
- Frequently test PowerBI Dataset through a list of DAX query to monitor dataset performance through time

## Installation

### Using pipx

```bash
pipx install powerbi-cli
```

### Using Docker

```bash
docker pull ghcr.io/lgrosjean/powerbi-cli:latest
```

## Usage

Please refer to the [sample documentation](./docs/samples/) for list of usages.


---

## References


- [`pbipy`](https://github.com/andrewvillazon/pbipy)
- [PowerBI REST API](https://learn.microsoft.com/en-us/rest/api/power-bi/)
- NodeJS `powerbi-cli` [source code](https://powerbi-cli.github.io/index.html)
- NodeJS `powerbi-cli` [documentation](https://github.com/powerbi-cli/powerbi-cli)