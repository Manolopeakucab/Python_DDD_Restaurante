from DDDAPI.Include.API.Plato.Domain.ValueOBjects.Plato_Pasos_VO import ValueObject
from typing import List

class Plato_Pasos_VO(ValueObject):
    
    pasos = List[str]

    def __init__(self, nombre):
        nombre = Plato_Pasos_VO.equals(nombre)
        if nombre is None:
            raise ValueError("Una receta tiene que tener mas de cero pasos")
        super().__init__()
        self.nombre = nombre

    def equals(self, other: 'Plato_Pasos_VO') -> bool:
        return self.pasos == other.pasos
    
    def valid(self) -> bool:
        return len(self.pasos) > 0
    
    def get_pasos(self) -> List[str]:
        return self 
    
    @staticmethod
    def create(pasos: List[str]) -> 'Plato_Pasos_VO':
        return Plato_Pasos_VO(pasos)