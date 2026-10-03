### Hexlet check
[![hexlet-check](https://github.com/pavelgrebenkov/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/pavelgrebenkov/python-project-50/actions/workflows/hexlet-check.yml)

### Github Actions CI
[![.github/workflows/python-check.yml](https://github.com/pavelgrebenkov/python-project-50/actions/workflows/python-check.yml/badge.svg)](https://github.com/pavelgrebenkov/python-project-50/actions/workflows/python-check.yml)

### SonarQube - maintainability rating
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=pavelgrebenkov_python-project-50&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=pavelgrebenkov_python-project-50)

### SonarQube - test coverage
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=pavelgrebenkov_python-project-50&metric=coverage)](https://sonarcloud.io/summary/new_code?id=pavelgrebenkov_python-project-50)

### Description:
This package was built as a requirement for the second academic module of the professional program, <em>Python Developer</em>, offered by <a href="https://ru.hexlet.io/" >Hexlet</a>, an online programming school.
The learning objectives of the project emphasised the following skills and knowledge areas:

- Software development environment setup
- Building correct package file structure
- Dependency management
- Selection of necessary libraries
- Code quality
- Code architecture and refactoring
- Debugging
- Writing tests with Pytest
- Preparing the application for publication
- Brief description and documentation of the application

### 1. Purpose:
A command-line tool that compares two structured configuration files and reports their differences in a user-selected format.

### 2. Inputs:
- Two file paths (positional arguments). Order matters: File 1 is the "original" or "old" version; File 2 is the "new" or "modified" version.
- An optional --format flag (values: stylish, plain, json). Default is stylish.
- File formats accepted: .json and .yaml / .yml.

### 3. Core logic rules:
- Parse both files into Python data structures (dictionaries, lists, strings, integers, booleans, None).
- For each key present in either structure, classify the difference as:
    * Added: key exists only in the new file.
    * Removed: key exists only in the old file.
    * Updated: key exists in both, but values differ (including type changes, e.g., int vs string).
    * Unchanged: key exists in both and values are strictly equal (same type and value).
- For nested structures, recurse deeply. If both values are dictionaries, recurse into them. If one is a dictionary and the other is not, treat as an update (type change) and do not recurse further.

### 4. Outputs formats:
- Stylish (default): A tree-like text using indentation and prefixes (+ for added, - for removed, space for unchanged). Shows the full nested structure for context. Keys are sorted alphabetically for stable output.
- Plain: A flat list of sentences in English (e.g., "Property 'key' was added with value: ..."). Only show keys that have changed (no unchanged lines). Use dot notation for nested paths (e.g., "group1.baz").
- JSON: A structured JSON array of difference objects, each containing at least type, key (or path), old value (if applicable), and new value (if applicable). Machine-readable.

### Requirements:
<ul>
  <li><a href="https://www.python.org/downloads/">Python 3.10</a> or higher</li>
  <li><a href=https://https://docs.astral.sh/uv/">uv</a></li>
</ul>

### Installation:
<ul>
  <li>To install the package type this command in the terminal:</li>
  <li><em>uv tool install git+<span>https://</span>github.com/pavelgrebenkov/python-project-49.git@refactor/project-restructure</em></li>
  <li>You can find all the information you need on how to install <em>uv</em><a href="https://docs.astral.sh/uv/getting-started/installation/"> here</a>.</li>
</ul>

### Video demonstrations:
To see how to install and uninstall the application, and how to use its various features, watch the demo videos below.
- [Installation/Uninstallation (with uv)](https://asciinema.org/a/1267381)
- [Parsing flat/nested files - stylish format](https://asciinema.org/a/6KeV2mCSoin3aAdi)
- [Parsing flat/nested files - plain format](https://asciinema.org/a/3i6Z6C4gmsZ7TGar)
- [Parsing flat/nested files - json format](https://asciinema.org/a/v8mQFReGeWGhxYUf)
