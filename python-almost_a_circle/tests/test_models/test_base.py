#!/usr/bin/python3
"""unittests for Base class"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test functions for base class"""

    def test_id_autogen(self):
        """Test auto generation of id for Base instance"""
        b = Base()
        self.assertTrue(b.id > 0)
        c = Base()
        self.assertEqual(c.id, b.id + 1)
