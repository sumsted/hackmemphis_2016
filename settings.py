import os

import yaml


class Settings:
    instance = None

    class __Settings:

        def __init__(self):
            with open(os.getenv('MEMPHIS_YAML', '')) as yaml_file:
                self.settings = yaml.load(yaml_file)

    def __init__(self):
        if Settings.instance is None:
            Settings.instance = self.__Settings()
        else:
            pass

    def __getattr__(self, item):
        if self.instance is not None:
            return self.instance.settings[item]
        else:
            return None

    def __setattr__(self, key, value):
        if self.instance is not None:
            self.instance.settings[key] = value

    def get(self, item, default=None):
        if self.instance is not None:
            if item in self.instance.settings:
                return self.instance.settings[item]
            else:
                return default
        else:
            return default

    def set(self, key, value):
        if self.instance is not None:
            self.instance.settings[key] = value

    def get_dict(self):
        if self.instance is not None:
            return self.instance.settings
