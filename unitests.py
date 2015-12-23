import unittest
from json import load

from file import read_tlp_file_config
from ui import create_tlp_ui_categories


def get_config_count(categories):
    configcount = 0
    for category in categories:
        configs = category['configs']
        configcount += len(configs);
    return configcount


class MyTestCase(unittest.TestCase):
    def test_config_categories(self):
        configfilelist = read_tlp_file_config("/etc/default/tlp")
        configfilecategories = create_tlp_ui_categories(configfilelist)

        self.assertEqual(len(configfilecategories), 12)

    def test_tlp_file_vs_json_config(self):
        # tlp file config
        configfilelist = read_tlp_file_config("/etc/default/tlp")

        # json config
        jsonfile = open('configcategories.json')
        jsonobject = load(jsonfile)
        jsoncategories = jsonobject['categories']
        jsonconfigcount = get_config_count(jsoncategories)

        self.assertEqual(len(configfilelist), 80)
        self.assertEqual(len(configfilelist), jsonconfigcount)


if __name__ == '__main__':
    unittest.main()