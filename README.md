# Base Template CLI

[![Test](https://github.com/haru52/base_template_cli/actions/workflows/test.yml/badge.svg)](https://github.com/haru52/base_template_cli/actions/workflows/test.yml)
[![Release](https://github.com/haru52/base_template_cli/actions/workflows/release.yml/badge.svg)](https://github.com/haru52/base_template_cli/actions/workflows/release.yml)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](CODE_OF_CONDUCT.md)
[![Commitizen friendly](https://img.shields.io/badge/commitizen-friendly-brightgreen.svg)](https://commitizen.github.io/cz-cli/)
[![semantic-release: conventionalcommits](https://img.shields.io/badge/semantic--release-conventionalcommits-e10079?logo=semantic-release)](https://github.com/semantic-release/semantic-release)

## Overview

CLI tool of [Base Template Repository](https://github.com/haru52/base_template#readme).

## Requirements

| Tool                                        | Version |
| ------------------------------------------- | ------- |
| Python                                      | ^3.10.5 |
| [Click](https://click.palletsprojects.com/) | ^8.1.3  |

## Installation

```sh
gh repo clone haru52/base_template_cli # Clone this repo
cd base_template_cli
make
```

## Usage

```console
Usage: base-template-cli [OPTIONS] BASE_TEMPLATE_ROOT_PATH

  Apply Base Template boilerplates to the destination repo.

Options:
  --version       Show the version and exit.
  -d, --dst TEXT  Destination repo root path.
  --dirs TEXT     Target directories to copy (e.g., .husky,
                  .github/ISSUE_TEMPLATE).
  -h, --help      Show this message and exit.
```

## Update

```sh
cd path/to/base_template_cli
git pull
```

## Uninstall

```sh
cd path/to/base_template_cli
make uninstall
cd ..
rm -rf base_template_cli
```

## Versioning

[Semantic Versioning 2.0.0](https://semver.org/spec/v2.0.0.html)

## License

[MIT](LICENSE)

## Contributing

[Contributing Guideline](CONTRIBUTING.md)

<!-- vale Microsoft.Vocab = NO -->

## Author
<!-- vale Microsoft.Vocab = YES -->

[haru](https://haru52.com/)
