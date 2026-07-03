.PHONY: gendiff install package-build package-install package-reinstall package-uninstall


# Test => only for testing CLI entry point (displays help information for the utility)
gendiff:
	uv run gendiff -h


# Dependencies => environment setup
install:
	uv sync


# Package => building/distributing/installing/uninstalling/listing
package-build:
	uv build

package-install:
	uv tool install dist/*.whl
	@echo "✅ Package successfully installed"

package-reinstall:
	uv tool install --force dist/*.whl
	@echo "✅ Package successfully reinstalled"

package-uninstall:
	uv tool uninstall hexlet-code
	@echo "✅ Package successfully uninstalled"
