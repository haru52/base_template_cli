import os

DEFAULT_TARGET_DIRS_DICT = {
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
    def __init__(
            self,
            base_template_updater,
            file_copy_util,
            dst_path,
            base_template_path,
            target_dirs):
        self.base_template_updater = base_template_updater
        self.file_copy_util = file_copy_util
        self.dst_path = dst_path
        self.base_template_path = base_template_path
        self.target_dirs = target_dirs

    def apply(self):
        self.base_template_updater.update()
        self.target_dirs_dict = self.__select_target_dirs_dict()
        self.__make_target_dirs()

        for dir, files in self.target_dirs_dict.items():
            if len(files) == 0:
                self.file_copy_util.copy_all_files(dir)
            else:
                self.file_copy_util.copy_files(dir, files)

        self.base_template_updater.revert()

    def __select_target_dirs_dict(self):
        if len(self.target_dirs) == 0:
            return DEFAULT_TARGET_DIRS_DICT

        selected_target_dir_tuples = [
            (d, f) for d, f in DEFAULT_TARGET_DIRS_DICT.items()
            if d in self.target_dirs]
        return dict(selected_target_dir_tuples)

    def __make_target_dirs(self):
        for dirs in self.target_dirs_dict:
            os.makedirs(os.path.join(self.dst_path, dirs), exist_ok=True)
