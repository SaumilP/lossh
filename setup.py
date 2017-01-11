from setuptools import find_packages
from setuptools import setup

MAJOR_VERSION = '0'
MINOR_VERSION = '1'
MICRO_VERSION = '1'
VERSION = "{}.{}.{}".format(MAJOR_VERSION, MINOR_VERSION, MICRO_VERSION)

setup(name='lossh',
      version=VERSION,
      description='Localhost share over SSH',
      author='Saumil Patel',
      url='',
      install_requires=[
        'click'
      ],
      entry_points={
        'console_scripts': ['lossh = lossh.lossh:main']
      },
      classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: SysAdmins',
        'Operating System :: Developers',
        'Topic :: Software Development',
        'Topic :: Utilities'
      ],
      platforms='any',
      packages=find_packages(),
      zip_safe=False)
