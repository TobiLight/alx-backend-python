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

    @patch("client.get_json", return_value={
        'name': 'repo1',
        'name': 'repo2'
    })
    def test_public_repos(self, mock_json: Mock) -> None:
        """
        Tests that the list of repos is what you expect from the chosen
        payload.
        """
        with patch("client.GithubOrgClient._public_repos_url",
                   new_callable=PropertyMock,
                   return_value="https://api.github.com/orgs/google/repos")\
                as mock_result:
            github_client = GithubOrgClient("google").public_repos()
            self.assertEqual(github_client, ["repo1", "repo2"])
            mock_json.assert_called_once()
            mock_result.assert_called_once()
