from therapy import queue
from therapy import rabbitmq

class SimpleQueue(queue.Queue):
    """docstring for SimpleQueue"""
    def perform(self):
        "Hello World"

SimpleQueue.use(library = rabbitmq.RabbitMQ)