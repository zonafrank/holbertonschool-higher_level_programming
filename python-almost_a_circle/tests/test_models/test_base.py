#!/usr/bin/python3
"""unittests for Base class"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_id_autogen(self):
        """Test auto generation of id for Base instance"""
        b = Base()
        # id_assigned = b > 0
        self.assertTrue(b.id > 0)
