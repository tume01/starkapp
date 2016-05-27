from repositories import ServiciosRepository
from repositories import ServicioTypesRepository

class ServiciosService(object):

    """docstring for ServiciosService"""

    __servicio_repository = ServiciosRepository.ServiciosRepository()
    __servicio_type_repository = ServicioTypesRepository.ServicioTypesRepository()

    def create(self, insert_data):
        return self.__servicio_repository.create(insert_data)

    def update(self, id, update_data):
        return self.__servicio_repository.update(id, update_data)

    def delete(self, id):

        update_data = {
            'deleted': True,
        }

        return self.update(id, update_data)

    def filter(self, filters):
        return self.__servicio_repository.filter(filters)

    def getServicios(self):
        return self.filter({'deleted': False})

    def getServicioTypes(self):
        return self.__servicio_type_repository.all()

    def findServicio(self, id):
        return self.__servicio_repository.find(id)