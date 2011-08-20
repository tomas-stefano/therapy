from distutils.core import setup, find_packages

setup(name='therapy', 
      version='0.0.1',
      description='Queue abstraction that is possible to use RabbitMQ, RestMQ, ActiveMQ or Beanstalkd in a simple solution',
      author="Tomás D'Stefano",
      author_email='tomas_stefano@sucessoft.com',
      url='https://github.com/tomas-stefano/therapy',
      download_url='https://github.com/tomas-stefano/therapy',
      keywords='queue rabbitmq activemq beanstalkd restmq message',
      packages=find_packages('src'),
      package_dir={'': 'src',},
      include_package_data=True)