from COMMON.Domain.aggregates.Aggregates import Aggregate
from ValueObjects.Id_Almacen_VO import Id_Almacen_VO
from ValueObjects.Nombre_VO import Nombre_Almacen_VO
from ValueObjects.Cantidad_Ingrediente_VO import Cantidad_Ingrediente_VO
from Events.Almacen_Creado import Almacen_Creado

class Almacen(Aggregate):
    def __init__(self, id_almacen: Id_Almacen_VO, nombre: Nombre_Almacen_VO, ingredientes: Cantidad_Ingrediente_VO):
        super().__init__()
        almacencreated= Almacen_Creado.create(id_almacen, nombre, ingredientes)

    def get_id(self) -> Id_Almacen_VO:
        return self._id_almacen
    
    def get_nombre(self) -> Nombre_Almacen_VO:
        return self._nombre
    
    def get_ingredientes(self) -> Cantidad_Ingrediente_VO:
        return self._ingredientes

    @staticmethod
    def create(id_almacen: Id_Almacen_VO, nombre: Nombre_Almacen_VO, ingredientes: Cantidad_Ingrediente_VO) -> 'Almacen':
        return Almacen(id_almacen, nombre, ingredientes)