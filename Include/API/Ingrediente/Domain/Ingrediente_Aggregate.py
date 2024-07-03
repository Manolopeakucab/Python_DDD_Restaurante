from Include.API.COMMON.Domain.aggregates.Aggregates import AggregateRoot
from Include.API.Ingrediente.Domain.ValueObjects.Id_Ingrediente_VO import Id_Ingrediente_VO
from Include.API.Ingrediente.Domain.ValueObjects.Nombre_ingrediente_VO import Nombre_Ingrediente_VO
from Include.API.Ingrediente.Domain.DomainEvent.Ingrediente_Creado_Event import Ingrediente_Creado_Event

class Ingrediente(AggregateRoot):
    
        def __init__(self, id_ingrediente: Id_Ingrediente_VO, nombre: Nombre_Ingrediente_VO, ):
            super().__init__()
            ingrediente = Ingrediente_Creado_Event.create(id_ingrediente, nombre)
            return ingrediente
    
        def get_id(self) -> Id_Ingrediente_VO:
            return self._id_ingrediente
    
        def get_nombre(self) -> Nombre_Ingrediente_VO:
            return self._nombre

    
        @staticmethod
        async def create(id_ingrediente: Id_Ingrediente_VO, nombre: Nombre_Ingrediente_VO) -> 'Ingrediente':
            return Ingrediente(id_ingrediente, nombre)