from COMMON.Domain.valueObjects import Value_object;
from Ingrediente.Domain.ValueObjects.Id_Ingrediente_VO import Id_Ingrediente_VO;

class Ingredientes_VO(Value_object):

    cantidad:int;
    ingrediente: Id_Ingrediente_VO;


    def __init__(self, cantidad: int, ingrediente: Id_Ingrediente_VO):
        cantidadc= Ingredientes_VO.valid(cantidad,ingrediente);
        if cantidadc is None:
            raise ValueError("La cantidad no puede ser menor o igual a 0")
        super().__init__()
        self._cantidad = cantidad
        self.ingrediente = ingrediente



    def equals(self, other: 'Ingredientes_VO') -> bool:
        return self._cantidad == other._cantidad & self._ingrediente == other._ingrediente
    
    def valid(self) -> bool:
        return self._cantidad > 0 & self._ingrediente != None
    
    def get_value(self) -> int:
        return self
    
    staticmethod
    def create(cantidad: int) -> 'Ingredientes_VO':
        return Ingredientes_VO(cantidad)