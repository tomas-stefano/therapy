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
            None # TODO: Need to raise something and pass a friendly msg
