import applyer

import file_copy_util


class DIManager:
    def __init__(self, dst_root_path, base_template_root_path, target_dirs):
        self.FileCopyUtil = file_copy_util.FileCopyUtil(
            dst_root_path, base_template_root_path)
        self.Applyer = applyer.Applyer(
            self.FileCopyUtil,
            dst_root_path,
            base_template_root_path,
            target_dirs)

    def getInstance(self, classname):
        return getattr(self, classname)
