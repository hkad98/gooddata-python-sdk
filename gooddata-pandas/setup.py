from setuptools import setup, find_packages

REQUIRES = ["gooddata-sdk==0.1", "pandas"]


def _read_version():
    with open("VERSION", "rt") as version_file:
        return version_file.readline().strip()


setup(
    name="gooddata-pandas",
    version=_read_version(),
    author="GoodData",
    license="MIT",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["tests"]),
)
