import json
import os


class VersionGetter:
    @staticmethod
    def get_version():
        PACKAGE_JSON_PATH = f'{os.path.dirname(__file__)}/../package.json'
        with open(PACKAGE_JSON_PATH, 'r') as package_json_f:
            package_json = json.load(package_json_f)

        return package_json['version']
