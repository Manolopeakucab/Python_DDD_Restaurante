from typing import Optional
from DDDAPI.Include.API.COMMON.Domain.domainevents.Domain_Event import DomainEvent
from DDDAPI.Include.API.Ingrediente.Domain.ValueObjects.Id_Ingrediente_VO import Id_Ingrediente_VO
from DDDAPI.Include.API.Ingrediente.Domain.ValueObjects.Nombre_ingrediente_VO import Nombre_Ingrediente_VO
from Include.API.Almacen.Domain.ValueObjects.Cantidad_Ingrediente_VO import Cantidad_Ingrediente_VO
from Include.API.Almacen.Domain.ValueObjects.Id_Almacen_VO import Id_Almacen_VO
class Ingrediente_Modificado_Event(DomainEvent):
    def __init__(self, id_ingrediente: Id_Ingrediente_VO, nombre: Nombre_Ingrediente_VO, cantidad: Cantidad_Ingrediente_VO, almacen: Id_Almacen_VO):
        super().__init__()
        self._id_ingrediente = id_ingrediente
        self._nombre = nombre
        self._cantidad = cantidad
        self._almacen = almacen

    @staticmethod
    def create(self, almacen: Id_Almacen_VO,id_ingrediente: Optional[Id_Ingrediente_VO] = None, nombre: Optional[Nombre_Ingrediente_VO] = None, cantidad: Optional[Cantidad_Ingrediente_VO] = None) -> 'Ingrediente_Modificado_Event':
        self.publish(self, 'ingrediente modificado en el almacen')
        return Ingrediente_Modificado_Event(almacen,id_ingrediente, nombre, cantidad)