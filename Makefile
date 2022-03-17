GENERATED_DIR ?= openapi
REMOVE_GENERATED_FILES ?= .openapi-generator test .gitlab-ci.yml .openapi-generator-ignore .gitignore .travis.yml git_push.sh 
SOURCE_FILES ?= $(shell find . -not -path "./$(GENERATED_DIR)/*" -type f -name '*.py' -print)
INPUT_SPECS ?= api sandbox

GIT_REVISION ?= $(shell git rev-parse --short HEAD)
GIT_TAG ?= $(shell git describe --tags --abbrev=0 | sed -e s/v//g)

.PHONY: help
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
.DEFAULT_GOAL := help

.PHONY: install-deps-dev
install-deps-dev: ## install dependencies for development

.PHONY: format
format: ## format codes

.PHONY: lint
lint: ## lint

.PHONY: test
test: ## run tests

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
ci-test: install-deps-dev generate generate-diff-check lint test ## ci test
