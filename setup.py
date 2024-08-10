from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Various functions to simplify common tasks'

setup(
    name="auralib",
    version=VERSION,
    author="GroundAura",
    author_email="<groundaura@gmail.com>",
    description=DESCRIPTION,
	license='Clear BSD',
    packages=find_packages(),
    install_requires=['configparser', 'os', 'shutil', 'subprocess'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3"
    ]
)