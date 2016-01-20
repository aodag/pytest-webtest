import pytest


@pytest.mark.webtest('example.ini')
def test_hello(webtest_app):
    res = webtest_app.get("/")
    assert "Hello, world!" == res.text
