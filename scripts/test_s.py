import pytest

class TestS:

    @pytest.skip(True ,reason=None)
    def test_s(self):
        print("skip")

    @pytest.mark.xfail(condition=True, reason="xx")
    def test_fail(self):
        print("")