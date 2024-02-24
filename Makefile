# Variables
APP_NAME=app
ROOT=$(shell pwd)

## Lint
DOCKER_IMAGE_LINTER=alvarofpp/linter:latest
LINT_COMMIT_TARGET_BRANCH=origin/main

## Test
TEST_CONTAINER_NAME=${APP_NAME}_test

# Commands
.PHONY: install-hooks
install-hooks:
	git config core.hooksPath .githooks

.PHONY: build
build: install-hooks
	@docker compose build --pull

.PHONY: build-no-cache
build-no-cache: install-hooks
	@docker compose build --no-cache --pull

.PHONY: lint
lint:
	@docker pull ${DOCKER_IMAGE_LINTER}
	@docker run --rm -v ${ROOT}:/app ${DOCKER_IMAGE_LINTER} " \
		lint-commit ${LINT_COMMIT_TARGET_BRANCH} \
		&& lint-markdown \
		&& lint-dockerfile \
		&& lint-yaml \
		&& lint-shell-script \
		&& lint-python"

.PHONY: test
test:
	@docker compose run --rm -v ${ROOT}:/app \
		--name ${TEST_CONTAINER_NAME} ${APP_NAME} \
		pytest

.PHONY: test-coverage
test-coverage:
	@docker compose run --rm -v ${ROOT}:/app \
		--name ${TEST_CONTAINER_NAME} ${APP_NAME} \
		/bin/bash -c "coverage run -m unittest discover tests && coverage report -m"

.PHONY: shell
shell:
	@docker compose run --rm ${APP_NAME} bash
