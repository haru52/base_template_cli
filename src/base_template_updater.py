import os
import subprocess


class BaseTemplateUpdater:
    def __init__(self, base_template_path):
        self.base_template_path = base_template_path
        self.stashed = False
        self.branch = 'main'

    def update(self):
        os.chdir(self.base_template_path)
        stash_result = subprocess.run(
            ['git', 'stash', '--include-untracked'],
            capture_output=True,
            text=True)
        stash_output = stash_result.stdout.strip()

        if ('no local changes to save' not in stash_output.lower()):
            self.stashed = True

        branch_result = subprocess.run(
            ['git', 'branch', '--show-current'],
            capture_output=True,
            text=True)
        self.branch = branch_result.stdout.strip()
        subprocess.run(['git', 'switch', 'main'])
        subprocess.run(['git', 'pull'])

    def revert(self):
        subprocess.run(['git', 'switch', self.branch])

        if not (self.stashed):
            return

        subprocess.run(['git', 'stash', 'pop'])
