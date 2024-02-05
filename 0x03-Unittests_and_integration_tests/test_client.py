#!/usr/bin/env python3
# File: test_client.py
# Author: Oluwatobiloba Light


import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test utils.GithubOrgClient"""

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    def test_org(self, test_org_name: str) -> None:
        """Tests that GithubOrgClient.org returns the correct value"""
        ret_val = {'payload': True}
        with patch("client.get_json", return_value={**ret_val}) as mock_result:
            github_client = GithubOrgClient(test_org_name)
            result = github_client.org
            self.assertEqual(result, mock_result.return_value)
            mock_result.assert_called_once_with(
                f'https://api.github.com/orgs/{test_org_name}')
