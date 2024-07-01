#!/usr/bin/env python3
"""module for testing the utils module."""
import unittest
from parameterized import parameterized
from utils import access_nested_map
from utils import get_json
from unittest.mock import patch, Mock
from utils import memoize


class TestAccessNestedMap(unittest.TestCase):
    """Test Nested maps"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """test access"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """test exeption"""
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(str(cm.exception), f"'{path[-1]}'")


class TestGetJson(unittest.TestCase):
    """Test Json"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """Test get json"""
        # Create a mock response object with a json method
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        # Call get_json and check the result
        result = get_json(test_url)
        self.assertEqual(result, test_payload)

        # Check that requests.get was called once with the test_url
        mock_get.assert_called_once_with(test_url)


class TestClass:
    """Test class"""
    def a_method(self):
        """a method"""
        return 42

    @memoize
    def a_property(self):
        """property"""
        return self.a_method()


class TestMemoize(unittest.TestCase):
    """Test memoize"""
    @patch.object(TestClass, 'a_method', return_value=42)
    def test_memoize(self, mock_a_method):
        """test"""
        test_instance = TestClass()

        # Call a_property twice
        result1 = test_instance.a_property
        result2 = test_instance.a_property

        # Check the results
        self.assertEqual(result1, 42)
        self.assertEqual(result2, 42)

        # Ensure a_method was called only once
        mock_a_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
