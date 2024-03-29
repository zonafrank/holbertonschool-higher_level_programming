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

    def test_id_specified(self):
        """Tests specified id for Base instance"""
        b = Base(89)
        self.assertEqual(b.id, 89)

    def test_to_json_string_none(self):
        """Testing to_json_string with None as argument"""
        str = Base.to_json_string(None)
        self.assertEqual(str, "[]")

    def test_to_json_string_empty_list(self):
        """Testing to_json_string with empty_ argumlistent"""
        str = Base.to_json_string([])
        self.assertEqual(str, "[]")

    def test_to_json_string_non_empty_list(self):
        """Testing to_json_string with non-empty list argument"""
        str = Base.to_json_string([{"id": 10}])
        self.assertEqual(str, "[{\"id\": 10}]")

    def test_from_json_string_none(self):
        """Testing from_json_string with None as argument"""
        lst = Base.from_json_string(None)
        self.assertEqual(lst, [])

    def test_from_json_string_empty_list(self):
        """Testing from_json_string with empty list string"""
        lst = Base.from_json_string("[]")
        self.assertEqual(lst, [])

    def test_from_json_string_list_with_content(self):
        """Testing from_json_string with list with content"""
        lst = Base.from_json_string("[{\"id\": 10}]")
        self.assertEqual(lst, [{"id": 10}])
