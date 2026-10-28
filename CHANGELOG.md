# Changelog

All notable changes to this project are described in this file.
The format is based on [Keep a Changelog](https://keepachangelog.com/uk/1.1.0/),
and versions follow [Semantic Versioning](https://semver.org/lang/uk/).

## [0.1.0] - 2026-10-28

### Added
- The `hello_bohdana` package with the `hello(name=“World”)` function.
- The `pyproject.toml` build configuration (setuptools, src-layout).
- The `mytest.service` systemd unit, which writes a line to `/tmp/test.log` every minute.
- A test server and the molotov load test.

### Fixed
- Added `.gitignore` to prevent the `dist/`, `build/`, and `*.egg-info` folders from being included in the repository.

### Security
- The package has no external dependencies, so it does not pull in any third-party code.
- The password for the local devpi is not stored in the repository.