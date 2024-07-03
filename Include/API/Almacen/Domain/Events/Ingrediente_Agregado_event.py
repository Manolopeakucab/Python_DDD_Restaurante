from Include.API.COMMON.Domain.domainevents import DomainEvent
from Include.API.Ingrediente.Domain.ValueObjects.Id_Ingrediente_VO import Id_Ingrediente_VO
from Include.API.Ingrediente.Domain.ValueObjects.Nombre_ingrediente_VO import Nombre_Ingrediente_VO
from Include.API.Almacen.Domain.ValueObjects.Cantidad_Ingrediente_VO import Cantidad_Ingrediente_VO
from Include.API.Almacen.Domain.ValueObjects.Id_Almacen_VO import Id_Almacen_VO
class Ingrediente_Agregado_Event(DomainEvent):
    def __init__(self, id_ingrediente: Id_Ingrediente_VO, nombre: Nombre_Ingrediente_VO, cantidad: Cantidad_Ingrediente_VO, almacen: Id_Almacen_VO):
        super().__init__()
        self._id_ingrediente = id_ingrediente
        self._nombre = nombre
        self._cantidad = cantidad
        self._almacen = almacen
        

    @staticmethod
    def create(self,id_ingrediente: Id_Ingrediente_VO, nombre: Nombre_Ingrediente_VO, cantidad: Cantidad_Ingrediente_VO, almacen: Id_Almacen_VO) -> 'Ingrediente_Agregado_Event':
        self.publish(self,'ingrediente añadido al almacen')
        return Ingrediente_Agregado_Event(id_ingrediente, nombre, cantidad, almacen)