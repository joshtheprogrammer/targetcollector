try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Joshua Ho Nguyen',
    'url': 'joshuahonguyen.com',
    'author_email': 'joshuahonguyen@gmail.com',
    'version': '0.1',
    'install_requires': [],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)