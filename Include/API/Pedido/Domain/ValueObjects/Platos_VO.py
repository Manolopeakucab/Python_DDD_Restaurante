from DDDAPI.Include.API.COMMON.Domain.valueObjects.Value_object import ValueObject
from DDDAPI.Include.API.Plato.Domain.ValueOBjects.Plato_Id_VO import Plato_Id_VO

class Platos_VO(ValueObject):
    
    plato:Plato_Id_VO;
    
    def __init__(self, plato:Plato_Id_VO):
        plato = Platos_VO.equals(plato)
        if plato is None:
            raise ValueError("El plato no puede ser vacio")
        super().__init__()
        self.plato = plato

    def equals(self, other: 'Platos_VO') -> bool:
        return self.plato == other.plato
    
    def valid(self) -> bool:
        return self.plato != 0
    
    def get_plato(self) -> Plato_Id_VO:
        return self.plato

    @staticmethod
    def create(plato: Plato_Id_VO) -> 'Platos_VO':
        return Platos_VO(plato)