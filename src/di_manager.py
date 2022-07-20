import applyer

import base_template_updater

import file_copy_util


class DIManager:
    def __init__(
            self,
            dst_root_path,
            base_template_root_path,
            target_dirs,
            only_root):
        self.BaseTemplateUpdater = base_template_updater.BaseTemplateUpdater(
            base_template_root_path)
        self.FileCopyUtil = file_copy_util.FileCopyUtil(
            dst_root_path, base_template_root_path)
        self.Applyer = applyer.Applyer(
            self.BaseTemplateUpdater,
            self.FileCopyUtil,
            dst_root_path,
            base_template_root_path,
            target_dirs,
            only_root)

    def getInstance(self, classname):
        return getattr(self, classname)
