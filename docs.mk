POETRY_RUN ?= poetry run
IP ?= localhost
PORT ?= 8000

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
.DEFAULT_GOAL := help

# https://python-poetry.org/docs/#osx--linux--bashonwindows-install-instructions
.PHONY: install-poetry
install-poetry: ## install poetry
	which poetry || curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

.PHONY: install-deps-dev
install-deps-dev: install-poetry ## install all dependencies including development
	poetry install

.PHONY: server
server: ## run server
	$(POETRY_RUN) mkdocs serve --dev-addr $(IP):$(PORT)

.PHONY: build
build: ## build site
	$(POETRY_RUN) mkdocs build

.PHONY: publish
publish: ## publish site
	$(POETRY_RUN) mkdocs gh-deploy --force

.PHONY: ci-test
ci-test: install-poetry install-deps-dev build ## ci test
