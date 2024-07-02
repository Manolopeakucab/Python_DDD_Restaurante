from DDDAPI.Include.API.COMMON.Domain.valueObjects import ValueObject
from DDDAPI.Include.API.Plato.Domain.ValueOBjects.Plato_Id_VO import Plato_Id_VO
from typing import List

class Platos_VO(ValueObject):

    def __init__(self,platos:list[Plato_Id_VO] ):
        super().__init__()
        self.platos = platos

    def equals(self, other: 'Platos_VO') -> bool:
        return self.platos == other.platos
    
    def valid(self) -> bool:
        return len(self.platos) > 0
    
    def get_platos(self) -> List[Plato_Id_VO]:
        return self.platos
    
    @staticmethod
    def create(platos: List[Plato_Id_VO]) -> 'Platos_VO':
        return Platos_VO(platos)