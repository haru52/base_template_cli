import os

TARGET_DIRS_DICT = {
    '': [],
    '.github': [],
    '.github/ISSUE_TEMPLATE': [],
    '.github/vale_styles/Vocab/Base': [],
    '.github/workflows': [],
    '.husky': [],
    '.vscode': ['extensions.json', 'settings.json'],
    'docs': [],
}

class Applyer:
    def __init__(self, file_copy_util, dst_path, base_template_path):
        self.file_copy_util = file_copy_util
        self.dst_path = dst_path
        self.base_template_path = base_template_path


    def apply(self):
        self.__make_target_dirs(self.dst_path)

        for dirs, files in TARGET_DIRS_DICT.items():
            if len(files) == 0:
                self.file_copy_util.copy_all_files(dirs)
            else:
                self.file_copy_util.copy_files(dirs, files)


    def __make_target_dirs(self, dst_path):
        for dirs in TARGET_DIRS_DICT:
            os.makedirs(os.path.join(dst_path, dirs), exist_ok=True)
