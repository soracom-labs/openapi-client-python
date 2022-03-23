[![test](https://github.com/soracom-labs/openapi-client-python/workflows/test/badge.svg)](https://github.com/soracom-labs/openapi-client-python/actions/workflows/test.yml)
[![release-drafter](https://github.com/soracom-labs/openapi-client-python/workflows/release-drafter/badge.svg)](https://github.com/soracom-labs/openapi-client-python/actions/workflows/release-drafter.yml)
[![gh-pages](https://github.com/soracom-labs/openapi-client-python/workflows/gh-pages/badge.svg)](https://github.com/soracom-labs/openapi-client-python/actions/workflows/gh-pages.yml)
[![labeler](https://github.com/soracom-labs/openapi-client-python/workflows/labeler/badge.svg)](https://github.com/soracom-labs/openapi-client-python/actions/workflows/labeler.yml)

# SORACOM API client for Python based on OpenAPI Generator

`soracom-labs/openapi-client-python` is a SORACOM API client for the Python programming language based on OpenAPI Generator.
This project only contains auto-generated codes from SORACOM API schema from OpenAPI Generator.

## Quick Start

### Look at some notebooks without executing any code

* <a href="https://nbviewer.jupyter.org/github/soracom-labs/openapi-client-python/blob/main/index.ipynb"><img src="https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg" alt="Render nbviewer" /></a>

### Run notebooks in locals

To run notebooks in locals, install dependencies first by the followings commands.

```bash
# if poetry is not installed yet.
make install-poetry

# install dependencies for the repo
make install-deps-dev
```

Virtual environment artifacts were created in `.venv` directory at the project root.

#### From browser

Just run the followings to open the default url in the browser

```console
make jupyterlab
```

#### From Visual Studio Code

Install [Jupyter extension](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) and open `*.ipynb` file.

## Documentation

Refer to the following docs for more detail about the client.

- [SORACOM API](https://soracom-labs.github.io/openapi-client-python/api/)
- [SORACOM API Sandbox](https://soracom-labs.github.io/openapi-client-python/sandbox/)

## Project Maturity

`soracom-labs/openapi-client-python` is based on OpenAPI Generator. This is under active development. We’re still working on implementing various kinds of features. We’re iterating fast and are likely to introduce breaking changes to existing APIs to improve the overall user experience of the product.

## Feedback

The `soracom-labs/openapi-client-python` will use GitHub Issues to track feature requests and issues with the client. You can provide feedback to us in the following way. 

**GitHub issues**. To provide feedback or report bugs, file GitHub Issues on the client. This is the preferred mechanism to give feedback so that other users can engage in the conversation, +1 issues, etc.

## Contributing
Please see [CONTRIBUTING](./.github/CONTRIBUTING.md) for detail.
