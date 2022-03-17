GENERATED_DIR ?= openapi
REMOVE_GENERATED_FILES ?= .openapi-generator test .gitlab-ci.yml .openapi-generator-ignore .gitignore .travis.yml git_push.sh 
SOURCE_FILES ?= $(shell find . -not -path "./.venv/*" -not -path "./$(GENERATED_DIR)/*" -type f -name '*.py' -print)
INPUT_SPECS ?= api sandbox

GIT_REVISION ?= $(shell git rev-parse --short HEAD)
GIT_TAG ?= $(shell git describe --tags --abbrev=0 | sed -e s/v//g)

SORACOM_PROFILE ?= ~/.soracom/default.json
SORACOM_AUTH_KEY ?= $(shell cat $(SORACOM_PROFILE) | jq -r .authKey)
SORACOM_AUTH_KEY_ID ?= $(shell cat $(SORACOM_PROFILE) | jq -r .authKeyId)

POETRY ?= poetry
POETRY_RUN ?= $(POETRY) run
POETRY_VENV_CREATE ?= true
POETRY_VENV_IN_PROJECT ?= true

IP ?= localhost
PORT ?= 8000

.PHONY: help
help:
	echo $(SOURCE_FILES)
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
.DEFAULT_GOAL := help

.PHONY: install-poetry
install-poetry: ## install poetry
	which poetry || pip install --user poetry
	$(POETRY) config virtualenvs.create $(POETRY_VENV_CREATE) --local
	$(POETRY) config virtualenvs.in-project $(POETRY_VENV_IN_PROJECT) --local

.PHONY: install-deps-dev
install-deps-dev: ## install all dependencies including development
	$(POETRY) install

.PHONY: format
format: ## format codes
	$(POETRY_RUN) isort $(SOURCE_FILES)
	$(POETRY_RUN) black $(SOURCE_FILES)

.PHONY: format-check
format-check: ## check code format
	$(POETRY_RUN) isort $(SOURCE_FILES) --check
	$(POETRY_RUN) black $(SOURCE_FILES) --check

.PHONY: lint
lint: ## lint
	$(POETRY_RUN) flake8 $(SOURCE_FILES)
	$(POETRY_RUN) mypy $(SOURCE_FILES)

.PHONY: test
test: ## run tests
	SORACOM_AUTH_KEY=$(SORACOM_AUTH_KEY) \
	SORACOM_AUTH_KEY_ID=$(SORACOM_AUTH_KEY_ID) \
	$(POETRY_RUN) pytest \
		--capture=no \
		--cov \
		--cov-branch \
		--verbose \
		$(SOURCE_FILES)

.PHONY: build
build: ## build package
	$(POETRY) build

.PHONY: release
release: ## release
	$(POETRY_RUN) twine upload --repository-url $(REPOSITORY_URL) dist/*

.PHONY: generate
generate: ## run OpenAPI Generator
	@for spec in $(INPUT_SPECS) ; do \
		make generate-spec INPUT_SPEC=$$spec ; \
    done

.PHONY: generate-spec
generate-spec: ## run OpenAPI Generator
	npx @openapitools/openapi-generator-cli generate \
		--input-spec specs/$(INPUT_SPEC).yaml \
		--generator-name python \
		--output $(GENERATED_DIR)/$(INPUT_SPEC) \
		--package-name $(INPUT_SPEC) \
		--git-host github.com \
		--git-user-id soracom-labs \
		--git-repo-id openapi-client-python \
		--http-user-agent openapi-client-python/$(GIT_TAG)
	cd $(GENERATED_DIR)/$(INPUT_SPEC) && rm -rf $(REMOVE_GENERATED_FILES)

.PHONY: generate-diff-check
generate-diff-check: ## check if generated codes are the same as tracked ones
	git diff --exit-code --relative $(GENERATED_DIR)

.PHONY: ci-test
ci-test: generate generate-diff-check install-poetry install-deps-dev format-check lint test build ## ci test

.PHONY: docs-server
docs-server: ## run docs server locally
	$(POETRY_RUN) mkdocs serve --dev-addr $(IP):$(PORT)

.PHONY: docs-build
docs-build: ## build site
	$(POETRY_RUN) mkdocs build

.PHONY: docs-release
docs-release: ## release docs
	$(POETRY_RUN) mkdocs gh-deploy --force
