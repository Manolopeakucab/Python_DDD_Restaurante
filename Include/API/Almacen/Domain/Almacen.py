from Include.API.COMMON.Domain.aggregates.Aggregates import Aggregate
from Include.API.Almacen.Domain.ValueObjects.Id_Almacen_VO import Id_Almacen_VO
from Include.API.Almacen.Domain.ValueObjects.Nombre_VO import Nombre_Almacen_VO
from Include.API.Almacen.Domain.ValueObjects.Cantidad_Ingrediente_VO import Cantidad_Ingrediente_VO
from Include.API.Almacen.Domain.Events.Almacen_Creado import Almacen_Creado
from Include.API.Almacen.Domain.Events.Ingrediente_Agregado_event import Ingrediente_Agregado_event
from Include.API.Almacen.Domain.Events.Ingrediente_Modificado_event import Ingrediente_Modificado_event
class Almacen(Aggregate):

    id: Id_Almacen_VO
    nombre:Nombre_Almacen_VO
    ingredientes: Cantidad_Ingrediente_VO

    def __init__(self, id_almacen: Id_Almacen_VO, nombre: Nombre_Almacen_VO, ingredientes: Cantidad_Ingrediente_VO):
        super().__init__(id, nombre, ingredientes)
        almacencreated= Almacen_Creado.create(id_almacen, nombre, ingredientes)
        return almacencreated

    def get_id(self) -> Id_Almacen_VO:
        return self._id_almacen
    
    def get_nombre(self) -> Nombre_Almacen_VO:
        return self._nombre
    
    def get_ingredientes(self) -> Cantidad_Ingrediente_VO:
        return self._ingredientes
    
    def ingrediente_Creado():
        pass

    def ingrediente_Modificado():
        pass
      

    @staticmethod
    async def create(id_almacen: Id_Almacen_VO, nombre: Nombre_Almacen_VO, ingredientes: Cantidad_Ingrediente_VO) -> 'Almacen':
        return Almacen(id_almacen, nombre, ingredientes)
    
    @staticmethod
    async def Ingrediente_add(id_almacen: Id_Almacen_VO,id_ingrediente: Cantidad_Ingrediente_VO, cantidad: Cantidad_Ingrediente_VO) -> 'Ingrediente_Agregado_event':
        return Ingrediente_Agregado_event(id_almacen,id_ingrediente, cantidad)
    
    @staticmethod
    async def Ingrediente_delete(id_almacen: Id_Almacen_VO,id_ingrediente: Cantidad_Ingrediente_VO, cantidad: Cantidad_Ingrediente_VO) -> 'Ingrediente_Modificado_event':
        return Ingrediente_Modificado_event(id_almacen,id_ingrediente,cantidad)