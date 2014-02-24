# coding: utf-8

from setuptools import setup, find_packages

setup(name='therapy',
      version='0.0.1',
      description='',
      long_description="""\
      """,
      author="Tomás D'Stefano",
      author_email='tomas_stefano@sucessoft.com',
      url='https://github.com/tomas-stefano/therapy',
      download_url='https://github.com/tomas-stefano/therapy',
      keywords='',
      license = "MIT License",
      packages=find_packages('therapy'),
      package_dir={'': 'src',},
      tests_require = ['nose >= 0.11'],
      test_suite = "nose.collector",
      include_package_data=True)