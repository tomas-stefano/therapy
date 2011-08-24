from tests.fixtures.rabbitmq import simple_queue
from tests.fixtures.rabbitmq import queue_without_library
from therapy import queue
from therapy import rabbitmq
from therapy import config
import unittest

class RabbitMQTest(unittest.TestCase):
    """describing SimpleQueue"""
    def setUp(self):
        self.queue = simple_queue.SimpleQueue()

    def test_should_perform_the_job_in_rabbit_mq(self):
        pass