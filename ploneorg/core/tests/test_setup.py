# -*- coding: utf-8 -*-
from plone import api
from ploneorg.core.testing import PLONEORG_CORE_INTEGRATION_TESTING

import unittest


PACKAGE_NAME = 'ploneorg.core'


class TestSetup(unittest.TestCase):

    layer = PLONEORG_CORE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

    def test_installation(self):
        quick_installer = api.portal.get_tool('portal_quickinstaller')
        installable_products = quick_installer.listInstallableProducts(
            skipInstalled=False
        )
        products = [p['id'] for p in installable_products]
        self.assertTrue(PACKAGE_NAME in products)
