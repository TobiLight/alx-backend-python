#!/usr/bin/env python3
# File: test_client.py
# Author: Oluwatobiloba Light
"""Test Client module"""


from typing import Dict
import unittest
from unittest.mock import Mock, PropertyMock, patch
from parameterized import parameterized, parameterized_class
from requests import HTTPError
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


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

    @patch("client.get_json")
    def test_public_repos(self, mock_json: Mock) -> None:
        """
        Tests that the list of repos is what you expect from the chosen
        payload.
        """
        test_payload = {
            'repos_url': "https://api.github.com/users/google/repos",
            'repos': [
                {
                    "id": 7697149,
                    "name": "episodes.dart",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342004,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/google/episodes.dart",
                    "created_at": "2013-01-19T00:31:37Z",
                    "updated_at": "2019-09-23T11:53:58Z",
                    "has_issues": True,
                    "forks": 22,
                    "default_branch": "master",
                },
                {
                    "id": 8566972,
                    "name": "kratu",
                    "private": False,
                    "owner": {
                        "login": "google",
                        "id": 1342004,
                    },
                    "fork": False,
                    "url": "https://api.github.com/repos/google/kratu",
                    "created_at": "2013-03-04T22:52:33Z",
                    "updated_at": "2019-11-15T22:22:16Z",
                    "has_issues": True,
                    "forks": 32,
                    "default_branch": "master",
                },
            ]
        }
        mock_json.return_value = test_payload['repos']
        with patch("client.GithubOrgClient._public_repos_url",
                   new_callable=PropertyMock) as mock_result:
            mock_result.return_value = test_payload["repos_url"]
            github_client = GithubOrgClient("google").public_repos()
            self.assertEqual(github_client, [
                "episodes.dart",
                "kratu",
            ])
            mock_result.assert_called_once()
            mock_json.assert_called_once()

    @parameterized.expand([
        ({'license': {'key': "bsd-3-clause"}}, "bsd-3-clause", True),
        ({'license': {'key': "bsl-1.0"}}, "bsd-3-clause", False),
    ])
    def test_has_license(self, repo: Dict, key: str, expected: bool) -> None:
        """Tests the `has_license` method."""
        gh_org_client = GithubOrgClient("google")
        client_has_licence = gh_org_client.has_license(repo, key)
        self.assertEqual(client_has_licence, expected)


@parameterized_class([
    {
        'org_payload': TEST_PAYLOAD[0][0],
        'repos_payload': TEST_PAYLOAD[0][1],
        'expected_repos': TEST_PAYLOAD[0][2],
        'apache2_repos': TEST_PAYLOAD[0][3],
    },
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Performs integration tests for the `GithubOrgClient` class."""
    @classmethod
    def setUpClass(cls) -> None:
        """Sets up class fixtures before running tests."""
        route_payload = {
            'https://api.github.com/orgs/google': cls.org_payload,
            'https://api.github.com/orgs/google/repos': cls.repos_payload,
        }

        def get_payload(url):
            if url in route_payload:
                return Mock(**{'json.return_value': route_payload[url]})
            return HTTPError

        cls.get_patcher = patch("requests.get", side_effect=get_payload)
        cls.get_patcher.start()

    def test_public_repos(self) -> None:
        """Tests the `public_repos` method."""
        self.assertEqual(
            GithubOrgClient("google").public_repos(),
            self.expected_repos,
        )

    def test_public_repos_with_license(self) -> None:
        """Tests the `public_repos` method with a license."""
        self.assertEqual(
            GithubOrgClient("google").public_repos(license="apache-2.0"),
            self.apache2_repos,
        )

    @classmethod
    def tearDownClass(cls) -> None:
        """Removes the class fixtures after running all tests."""
        cls.get_patcher.stop()
