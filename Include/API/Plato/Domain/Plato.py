from Include.API.COMMON.Domain.aggregates.Aggregates import AggregateRoot
from Include.API.Plato.Domain.ValueOBjects.Plato_Ingredientes_VO import Plato_Ingredientes_VO
from Include.API.Plato.Domain.ValueOBjects.Plato_Nombre_VO import Plato_Nombre_VO
from Include.API.Plato.Domain.ValueOBjects.Plato_Id_VO import Plato_Id_VO
from Include.API.Plato.Domain.ValueOBjects.Plato_Pasos_VO import Plato_Pasos_VO 
from Include.API.Plato.Domain.DomainEvents.Plato_Creado_Event import Plato_Creado_Event


class Plato(AggregateRoot):
    id: Plato_Id_VO
    nombre: Plato_Nombre_VO
    ingredientes: Plato_Ingredientes_VO
    pasos: Plato_Pasos_VO

    def __init__(self, id: Plato_Id_VO, nombre: Plato_Nombre_VO, ingredientes: Plato_Ingredientes_VO, pasos: Plato_Pasos_VO):
        super().__init__()
        plato = Plato_Creado_Event.create(id, nombre, ingredientes, pasos)
        return plato
    
    def get_id(self) -> Plato_Id_VO:
        return self.id
    
    def get_nombre(self) -> Plato_Nombre_VO:
        return self.nombre
    
    def get_ingredientes(self) -> Plato_Ingredientes_VO:    
        return self.ingredientes
    
    def get_pasos(self) -> Plato_Pasos_VO:
        return self.pasos
    
    @staticmethod
    async def create(id: Plato_Id_VO, nombre: Plato_Nombre_VO, ingredientes: Plato_Ingredientes_VO, pasos: Plato_Pasos_VO) -> 'Plato':
        return Plato(id, nombre, ingredientes, pasos)
        