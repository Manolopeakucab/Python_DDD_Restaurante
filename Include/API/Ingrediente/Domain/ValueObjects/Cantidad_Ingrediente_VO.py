from COMMON.Domain.valueObjects import Value_object;

class Cantidad_Ingrediente_VO(Value_object):

    cantidad:int;

    def __init__(self, cantidad: int):
        cantidadc= Cantidad_Ingrediente_VO.valid(cantidad);
        if cantidadc is None:
            raise ValueError("La cantidad no puede ser menor o igual a 0")
        super().__init__()
        self._cantidad = cantidad

    def equals(self, other: 'Cantidad_Ingrediente_VO') -> bool:
        return self._cantidad == other._cantidad
    
    def valid(self) -> bool:
        return self._cantidad > 0
    
    def get_value(self) -> int:
        return self
    
    staticmethod
    def create(cantidad: int) -> 'Cantidad_Ingrediente_VO':
        return Cantidad_Ingrediente_VO(cantidad)