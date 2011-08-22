from tests.fixtures.rabbitmq import simple_queue
from tests.fixtures.rabbitmq import queue_without_library
from therapy import queue
from therapy import rabbitmq
import unittest

class RabbitMQTest(unittest.TestCase):
    """describing SimpleQueue"""
    def setUp(self):
        """initializing SimpleQueue"""
        self.queue = simple_queue.SimpleQueue()
    
    def test_should_return_rabbitmq_as_simple_queue_library(self):
        """should return rabbitmq as queue library"""
        self.assertEqual(rabbitmq.RabbitMQ, simple_queue.SimpleQueue.library())

    def test_should_return_none_when_not_have_library_to_use(self):
        """test should return none when not have library to use"""
        self.assertRaises(queue.WithoutQueueLibraryError, queue_without_library.QueueWithoutLibrary.library)
            
