import abc

class AbstractBaseRepository(object):
    __metaclass__ = abc.ABCMeta

    __model = None

    @abc.abstractmethod
    def setUpModel(self):
        """Set up the repository model"""

    @abc.abstractmethod
    def all(self):
        """Get all elements"""

    @abc.abstractmethod
    def find(self, id):
        """Find an element"""

    @abc.abstractmethod
    def create(self, insert_data):
        """Create an element"""

    @abc.abstractmethod
    def update(self, id, update_data):
        """Update an element"""

    @abc.abstractmethod
    def delete(self, id):
        """Delete an element"""
