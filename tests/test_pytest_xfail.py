import pytest

@pytest.mark.xfail(reason="There is a known bug and test fails with an error")
def test_with_bug():
    assert 1 == 2

@pytest.mark.xfail(reason="Bug is Fixed but there the test is still marked")
def test_without_bug():
    pass
