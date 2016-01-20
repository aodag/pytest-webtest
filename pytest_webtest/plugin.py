#
import os.path

from paste.deploy import loadwsgi
import pytest
import webtest


def pytest_addoption(parser):
    parser.addoption('--paster-ini', default='development.ini')


@pytest.fixture
def webtest_app(request):
    relative_to = None
    if "webtest" in request.keywords:
        inifile = request.keywords["webtest"].args[0]
        relative_to = os.path.dirname(request.module.__file__)
    else:
        inifile = request.config.inifile
        inifile = os.path.abspath(os.path.normpath(inifile))
    app = loadwsgi.loadapp(
        "config:" + inifile,
        relative_to=relative_to)
    return webtest.TestApp(app)
