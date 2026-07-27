.PHONY: gendiff install update lint lint-fix test test-coverage package-build package-publish package-install-github package-install package-reinstall package-uninstall package-list-local package-list-global


# Test => only for testing CLI entry point (displays help information for the utility)
gendiff:
	uv run gendiff -h


# Dependencies => environment setup
install:
	uv sync

update:
	uv sync --upgrade


# Lint => code quality
lint:
	uv run ruff check gendiff

lint-fix:
	uv run ruff check --fix gendiff


# Pytest => code functionality
test:
	uv run pytest -vv

test-coverage:
	uv run pytest --cov=gendiff --cov-report xml


# Package => building/distributing/installing/uninstalling/listing
package-build:
	uv build

package-publish:
	uv publish --dry-run

# Install the package from GitHub
package-install-github:
	uv tool install git+https://github.com/pavelgrebenkov/python-project-50.git

package-install:
	uv tool install dist/*.whl
	@echo "✅ Package successfully installed"

package-reinstall:
	uv tool install --force dist/*.whl
	@echo "✅ Package successfully reinstalled"

package-uninstall:
	uv tool uninstall hexlet-code
	@echo "✅ Package successfully uninstalled"

# Lists packages in the current virtual environment
package-list-local:
	uv pip list

# Lists globally installed tools
package-list-global:
	uv tool list
