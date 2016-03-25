try:
  from setuptools import setup
except ImportError:
  from distutils.core import setup

setup(
    name="soupselect",
    version="0.0.0",
    description="CSS Selectors for BeautifulSoup",
    url="https://github.com/martinezah/soupselect",
    author="Maintained by Marti Martinez",
    author_email="martinezah@gmail.com",
    packages=[
    "soupselect"
    ],
)
