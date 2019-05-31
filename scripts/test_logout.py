import pytest


class TestLogout:

    def setup(self):
        print("setup")

    def teardown(self):
        print("teardown")

    def test_logout(self):
        print("logout")
