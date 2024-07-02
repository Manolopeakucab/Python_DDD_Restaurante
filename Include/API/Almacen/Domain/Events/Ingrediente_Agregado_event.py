from COMMON.Domain.domainevents.Domain_Event import DomainEvent
from Ingrediente.Domain.ValueObjects.Id_Ingrediente_VO import Id_Ingrediente_VO
from Ingrediente.Domain.ValueObjects.Nombre_ingrediente_VO import Nombre_Ingrediente_VO
from Include.API.Almacen.Domain.ValueObjects.Cantidad_Ingrediente_VO import Cantidad_Ingrediente_VO

class Ingrediente_Agregado_Event(DomainEvent):
    def __init__(self, id_ingrediente: Id_Ingrediente_VO, nombre: Nombre_Ingrediente_VO, cantidad: Cantidad_Ingrediente_VO):
        super().__init__()
        self._id_ingrediente = id_ingrediente
        self._nombre = nombre
        self._cantidad = cantidad

    @staticmethod
    def create(id_ingrediente: Id_Ingrediente_VO, nombre: Nombre_Ingrediente_VO, cantidad: Cantidad_Ingrediente_VO) -> 'Ingrediente_Agregado_Event':
        return Ingrediente_Agregado_Event(id_ingrediente, nombre, cantidad)