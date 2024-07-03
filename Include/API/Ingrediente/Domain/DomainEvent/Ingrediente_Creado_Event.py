from Include.API.COMMON.Domain.domainevents.Domain_Event import DomainEvent
from  Include.API.Ingrediente.Domain.ValueObjects.Id_Ingrediente_VO import Id_Ingrediente_VO
from Include.API.Ingrediente.Domain.ValueObjects.Nombre_ingrediente_VO import Nombre_Ingrediente_VO

class Ingrediente_Creado_Event(DomainEvent):
    def __init__(self, id_ingrediente: Id_Ingrediente_VO, nombre: Nombre_Ingrediente_VO):
        super().__init__()
        self._id_ingrediente = id_ingrediente
        self._nombre = nombre

    staticmethod
    def create(self,id_ingrediente: Id_Ingrediente_VO, nombre: Nombre_Ingrediente_VO) -> 'Ingrediente_Creado_Event':
        self.publish(self,'Ingrediente añadido')
        return Ingrediente_Creado_Event(id_ingrediente, nombre)