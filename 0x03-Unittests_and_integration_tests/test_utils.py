#!/usr/bin/env python3
# File:test_utils.py
# Author: Oluwatobiloba Light


from typing import Dict
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json
from unittest.mock import MagicMock, Mock, patch


class TestAccessNestedMap(unittest.TestCase):
    """Test access nested map Object"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test Access nested map with key path"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ('a', ), KeyError('a')),
        ({'a': 1}, ('a', 'b'), KeyError('b')),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """Test Access nested map with exception"""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)

        exception_message = str(context.exception)
        self.assertEqual(exception_message, str(expected))


class TestGetJSON(unittest.TestCase):
    """Test GetJSON method"""
    @parameterized.expand([
        ("http://example.com", {'payload': True}),
        ("http://holberton.io", {'payload': False})
    ])
    def test_get_json(self, test_url: str, payload: Dict) -> None:
        """Tests that utils.get_json returns the expected result."""
        json_return = {'json.return_value': payload}
        with patch('utils.requests.get', return_value=Mock(**json_return)) as\
                mock_get:
            result = get_json(test_url)
            mock_get.assert_called_once_with(test_url)
            self.assertEqual(result, payload)
