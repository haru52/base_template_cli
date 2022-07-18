import os
import file_copy_util

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
    def __init__(self, dst_path, base_template_path):
        self.dst_path = dst_path
        self.base_template_path = base_template_path
        self.file_copy_manager = file_copy_util.FileCopyUtil(self.dst_path, self.base_template_path)


    def apply(self):
        self.__make_target_dirs(self.dst_path)

        for dirs, files in TARGET_DIRS_DICT.items():
            if len(files) == 0:
                self.file_copy_manager.copy_all_files(dirs)
            else:
                self.file_copy_manager.copy_files(dirs, files)


    def __make_target_dirs(self, dst_path):
        for dirs in TARGET_DIRS_DICT:
            os.makedirs(os.path.join(dst_path, dirs), exist_ok=True)
