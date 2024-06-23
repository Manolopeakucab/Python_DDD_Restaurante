from COMMON.Domain.valueObjects import ValueObject
from Ingrediente.Domain.ValueObjects.Id_Ingrediente_VO import Id_Ingrediente_VO
from typing import List

class Plato_Ingredientes_VO(ValueObject):

    def __init__(self, ingredientes: List[Id_Ingrediente_VO]):
        ingredientes = Plato_Ingredientes_VO.valid(ingredientes)
        if ingredientes is None:
            raise ValueError("El plato tiene que tener ingredientes")
        super().__init__()
        self.ingredientes = ingredientes
    
    def equals(self, other: 'Plato_Ingredientes_VO') -> bool:
        return self.ingredientes == other.ingredientes
    
    def valid(self) -> bool:
        return len(self.ingredientes) > 0