import configparser
import os


class Section:
    def __init__(self, config, section_name):
        object.__setattr__(self, "_config", config)
        object.__setattr__(self, "_section", section_name)

        # auto-create section
        if not config._parser.has_section(section_name):
            config._parser.add_section(section_name)
            config.save()

    def __getattr__(self, key):
        return self._config._parser[self._section].get(key, "")

    def __setattr__(self, key, value):
        self._config._parser[self._section][key] = str(value)
        self._config.save()


class ini_conf:
    def __init__(self, filename="config.ini"):
        self._parser = configparser.ConfigParser()

        base_dir = os.path.dirname(os.path.abspath(__file__))
        self._filename = os.path.join(base_dir, filename)

        if os.path.exists(self._filename):
            self._parser.read(self._filename)

    def __getattr__(self, section):
        return Section(self, section)

    def save(self):
        with open(self._filename, "w") as f:
            self._parser.write(f)