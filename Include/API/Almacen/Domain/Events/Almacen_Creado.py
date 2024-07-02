from DDDAPI.Include.API.COMMON.Domain.domainevents.Domain_Event import DomainEvent
from DDDAPI.Include.API.Almacen.Domain.ValueObjects.Id_Almacen_VO import Id_Almacen_VO
from DDDAPI.Include.API.Almacen.Domain.ValueObjects.Nombre_VO import Nombre_Almacen_VO
from DDDAPI.Include.API.Almacen.Domain.ValueObjects.Cantidad_Ingrediente_VO import Cantidad_Ingrediente_VO


class Almacen_Creado(DomainEvent):
    def __init__(self, id_almacen: Id_Almacen_VO, nombre: Nombre_Almacen_VO, ingredientes: Cantidad_Ingrediente_VO):
        self.id_almacen = id_almacen
        self.nombre = nombre
        self.ingredientes = ingredientes
        

    @staticmethod
    def create(self, id_almacen: Id_Almacen_VO, nombre: Nombre_Almacen_VO, ingredientes: Cantidad_Ingrediente_VO) -> 'Almacen_Creado':
        self.publish(self,'almacen creado')
        return Almacen_Creado(id_almacen, nombre, ingredientes)