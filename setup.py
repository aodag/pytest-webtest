from setuptools import setup, find_packages


requires = [
    "pytest",
    "webtest",
    "pastedeploy",
]

tests_require = [
]


setup(
    name="pytest-webtest",
    install_requires=requires,
    tests_require=tests_require,
    extras_require={
        "testing": tests_require,
    },
)
