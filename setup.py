from setuptools import setup, find_packages


requires = [
    "pytest",
    "webtest",
    "pastedeploy",
]

tests_require = [
]

points = {
    'pytest11': [
        "webtest = pytest_webtest.plugin",
    ],
}

setup(
    name="pytest-webtest",
    install_requires=requires,
    tests_require=tests_require,
    extras_require={
        "testing": tests_require,
    },
    entry_points=points,
)
