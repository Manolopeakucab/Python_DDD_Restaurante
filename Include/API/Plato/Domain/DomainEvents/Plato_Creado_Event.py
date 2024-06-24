from DDDAPI.Include.API.COMMON.Domain.domainevents.Domain_Event import DomainEvent
from DDDAPI.Include.API.Plato.Domain.ValueOBjects.Plato_Id_VO import Plato_Id_VO
from DDDAPI.Include.API.Plato.Domain.ValueOBjects.Plato_Nombre_VO import Plato_Nombre_VO
from DDDAPI.Include.API.Plato.Domain.ValueOBjects.Plato_Ingredientes_VO import Plato_Ingredientes_VO
from DDDAPI.Include.API.Plato.Domain.ValueOBjects.Plato_Pasos_VO import Plato_Pasos_VO

class Plato_Creado_Event(DomainEvent):
    def __init__(self, id_plato: Plato_Id_VO, nombre: Plato_Nombre_VO, ingredientes:Plato_Ingredientes_VO, pasos: Plato_Pasos_VO):
        super().__init__()
        self._id_plato = id_plato
        self._nombre = nombre
        self._ingredientes = ingredientes
        self._pasos = pasos

    staticmethod
    def create(id_plato: Plato_Id_VO, nombre: Plato_Nombre_VO, ingredientes:Plato_Ingredientes_VO, pasos: Plato_Pasos_VO) -> 'Plato_Creado_Event':
        return Plato_Creado_Event(id_plato, nombre, ingredientes, pasos)