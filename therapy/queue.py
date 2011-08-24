class Queue(object):
    """docstring for Queue"""
    @classmethod
    def use(klass, library=None):
        """Return the library used by Therapy users"""
        klass.library_to_use = library
        return klass.library_to_use
    
    @classmethod
    def library(klass):
        """docstring for library"""
        try:
            return klass.library_to_use
        except:
            raise WithoutQueueLibraryError("You need to pass a library to use. Example: MyQueue.use(library = RestMQ) -> Or RabbitMQ, ActiveMQ, BeanStalkd")

class WithoutQueueLibraryError(Exception):
    def __init__(self, text):
        self.text = text
    
    def __str__(self):
        return repr(self.text)