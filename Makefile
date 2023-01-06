.PHONY: install uninstall dev-install lint lint-npm lint-text lint-yaml lint-sh lint-action lint-py
.PHONY: format format-npm format-py update-gi

install:
	bin/install.sh

uninstall:
	rm -f ~/bin/base-template-cli

dev-install:
	npm ci
	vale sync
	pipenv install --dev

lint: lint-npm lint-text lint-yaml lint-sh lint-action lint-py

lint-npm:
	npm run lint

lint-text:
	vale README.md docs/CONTRIBUTING.md docs/SECURITY.md .github/*.md .github/ISSUE_TEMPLATE

lint-yaml:
	yamllint --strict .

lint-sh:
	shellcheck .husky/commit-msg .husky/pre-commit bin/*.sh

lint-action:
	actionlint

lint-py:
	pipenv run lint

format: format-npm format-py

format-npm:
	npm run format

format-py:
	pipenv run format

update-gi:
	gibo update
	cat .gitignore_custom >| .gitignore
	gibo dump macOS Linux Windows VisualStudioCode JetBrains Vim Node Python >> .gitignore
