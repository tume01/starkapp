class AbstractBaseRepository():
    __model = None

    def __init__(self):
        """init"""

    def setUpModel(self):
        """Set up the repository model"""

    def all(self):
        """Get all elements"""

    def find(self, id):
        """Find an element"""

    def create(self, insert_data):
        """Create an element"""

    def update(self, id, update_data):
        """Update an element"""

    def delete(self, id):
        """Delete an element"""
