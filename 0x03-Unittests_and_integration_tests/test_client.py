#!/usr/bin/env python3
# File: test_client.py
# Author: Oluwatobiloba Light


import unittest
from unittest.mock import Mock, PropertyMock, patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test utils.GithubOrgClient"""

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch("client.get_json", return_value={'payload': True})
    def test_org(self, test_org_name: str, mock_result: Mock) -> None:
        """Tests that GithubOrgClient.org returns the correct value"""
        github_client = GithubOrgClient(test_org_name)
        result = github_client.org
        self.assertEqual(result, mock_result.return_value)
        mock_result.assert_called_once_with(
            f'https://api.github.com/orgs/{test_org_name}')

    def test_public_repos_url(self):
        """
        Tests that the result of _public_repos_url is the expected one based
        on the mocked payload.
        """
        with patch("client.GithubOrgClient.org", new_callable=PropertyMock,
                   return_value={"repos_url":
                                 "https://api.github.com/orgs/google/repos"})\
                as mock_result:
            github_client = GithubOrgClient("google")
            self.assertEqual(github_client._public_repos_url,
                             mock_result.return_value["repos_url"])
