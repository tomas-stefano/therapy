# coding: utf-8

from setuptools import setup, find_packages

setup(name='therapy', 
      version='0.0.1',
      description='Queue abstraction that is possible to use RabbitMQ, RestMQ, ActiveMQ or Beanstalkd in a simple solution',
      long_description="""\
        Queue abstraction that is possible to use RabbitMQ, RestMQ, ActiveMQ or Beanstalkd in a simple class. 
        You only need to do is respect/use the contract given by the Queue Class.
      """,
      author="Tomás D'Stefano",
      author_email='tomas_stefano@sucessoft.com',
      url='https://github.com/tomas-stefano/therapy',
      download_url='https://github.com/tomas-stefano/therapy',
      keywords='queue rabbitmq activemq beanstalkd restmq message',
      license = "MIT License",
      packages=find_packages('lib'),
      package_dir={'': 'lib',},
      tests_require = ['nose >= 0.11'],
      test_suite = "nose.collector",
      include_package_data=True)