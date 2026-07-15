### Hexlet tests and linter status:
[![Actions Status](https://github.com/pavelgrebenkov/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/pavelgrebenkov/python-project-50/actions)

### Qlty & SonarQube - maintainability rating
[![Qlty check](https://qlty.sh/gh/pavelgrebenkov/projects/python-project-50/maintainability.svg)](https://qlty.sh/gh/pavelgrebenkov/projects/python-project-50)
[![SonarQube check](https://sonarcloud.io/api/project_badges/measure?project=pavelgrebenkov_python-project-50&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=pavelgrebenkov_python-project-50)

### Description:
<p>
This package was built as a requirement for the second academic module of the professional program, <em>Python Developer</em>, offered by <a href="https://ru.hexlet.io/" >Hexlet</a>, an online programming school.
The learning objectives of the project emphasised the following skills and knowledge areas:
</p>
<ul>
  <li>Software development environment setup</li>
  <li>Building correct package file structure</li>
  <li>Dependency management</li>
  <li>Selection of necessary libraries</li>
  <li>Code quality</li>
  <li>Code architecture and refactoring</li>
  <li>Debugging</li>
  <li>Writing tests with Pytest</li>
  <li>Preparing the application for publication</li>
  <li>Brief description and documentation of the application</li>
</ul>

### 1. Purpose:
<p>
A command-line tool that compares two structured configuration files and reports their differences in a user-selected format.
<p>

### 2. Inputs:
<ul>
  <li>Two file paths (positional arguments). Order matters: File 1 is the "original" or "old" version; File 2 is the "new" or "modified" version.</li>
  <li>An optional --format flag (values: stylish, plain, json). Default is stylish.</p>
  <li>File formats accepted: .json and .yaml / .yml.</p>
</ul>

### 3. Core logic rules:
<ul>
  <li>Parse both files into Python data structures (dictionaries, lists, strings, integers, booleans, None).</li>
  <li>For each key present in either structure, classify the difference as:<li>
  <ul>
    <li>Added: key exists only in the new file.</li>
    <li>Removed: key exists only in the old file.</li>
    <li>Updated: key exists in both, but values differ (including type changes, e.g., int vs string).</li>
    <li>Unchanged: key exists in both and values are strictly equal (same type and value).</li>
  </ul>
  <li>For nested structures, recurse deeply. If both values are dictionaries, recurse into them. If one is a dictionary and the other is not, treat as an update (type change) and do not recurse further.<li>
</ul>

### 4. Outputs formats:
<ul>
  <li>Stylish (default): A tree-like text using indentation and prefixes (+ for added, - for removed, space for unchanged). Shows the full nested structure for context. Keys are sorted alphabetically for stable output.</li>
  <li>Plain: A flat list of sentences in English (e.g., "Property 'key' was added with value: ..."). Only show keys that have changed (no unchanged lines). Use dot notation for nested paths (e.g., "group1.baz").</li>
  <li>JSON: A structured JSON array of difference objects, each containing at least type, key (or path), old value (if applicable), and new value (if applicable). Machine-readable.</li>
</ul>
