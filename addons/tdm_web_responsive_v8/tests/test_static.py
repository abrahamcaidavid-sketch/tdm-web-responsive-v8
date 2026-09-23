# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import ast
import os
import unittest
from xml.etree import ElementTree


MODULE_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class ResponsiveModuleStaticTest(unittest.TestCase):

    def test_manifest_targets_odoo_8_and_web_only(self):
        manifest_path = os.path.join(MODULE_ROOT, '__openerp__.py')
        with open(manifest_path, 'rb') as manifest_file:
            manifest = ast.literal_eval(manifest_file.read().decode('utf-8'))

        self.assertTrue(manifest['version'].startswith('8.0.'))
        self.assertEqual(manifest['depends'], ['web'])
        self.assertTrue(manifest['installable'])

    def test_xml_files_are_well_formed(self):
        for relative_path in ('views/assets.xml', 'views/webclient.xml'):
            ElementTree.parse(os.path.join(MODULE_ROOT, relative_path))

    def test_required_static_assets_exist(self):
        for relative_path in (
                'static/src/css/responsive.css',
                'static/src/js/responsive.js'):
            self.assertTrue(os.path.isfile(os.path.join(MODULE_ROOT,
                                                        relative_path)))


if __name__ == '__main__':
    unittest.main()

