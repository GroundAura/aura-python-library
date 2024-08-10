from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    LONG_DESCRIPTION = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'Various functions to simplify common tasks'

setup(
    name="auralib",
    version=VERSION,
    author="GroundAura",
    author_email="<groundaura@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
	license='Clear BSD',
    packages=find_packages(),
    install_requires=['configparser', 'os', 'shutil', 'subprocess'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3"
    ]
)