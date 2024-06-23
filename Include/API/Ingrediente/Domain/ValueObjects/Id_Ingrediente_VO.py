from COMMON.Domain.valueObjects import Value_object;

class Id_Ingrediente_VO(Value_object):

    id_ingrediente:int;

    def __init__(self, id_ingrediente: int):
        id_ingrediente = Id_Ingrediente_VO.valid(id_ingrediente);
        if id_ingrediente is None:
            raise ValueError("El id del ingrediente no puede ser menor o igual a 0")
        self._id_ingrediente = id_ingrediente

    def equals(self, other: 'Id_Ingrediente_VO') -> bool:
        return self._id_ingrediente == other._id_ingrediente
    
    def valid(self) -> bool:
        return self._id_ingrediente > 0
    
    def get_value(self) -> str:
        return self
    
    staticmethod
    def create(id_ingrediente: str) -> 'Id_Ingrediente_VO':
        return Id_Ingrediente_VO(id_ingrediente)
