from therapy import queue
from therapy import rabbitmq

class SimpleQueue(rabbitmq.RabbitMQ):
    """docstring for SimpleQueue"""
    def perform(self):
        "Hello World"

