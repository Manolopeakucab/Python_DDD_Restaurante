from Include.API.COMMON.Domain.valueObjects import Value_object;

class Nombre_Ingrediente_VO(Value_object):

    nombre:str;

    def __init__(self, nombre: str):
        nombre = Nombre_Ingrediente_VO.valid(nombre);
        if nombre is None:
            raise ValueError("El nombre del ingrediente no puede ser vacio")
        self._nombre = nombre

    def equals(self, other: 'Nombre_Ingrediente_VO') -> bool:
        return self._nombre == other._nombre
    
    def valid(self) -> bool:
        return len(self._nombre) > 0
    
    def get_value(self) -> str:
        return self
    
    staticmethod
    def create(nombre: str) -> 'Nombre_Ingrediente_VO':
        return Nombre_Ingrediente_VO(nombre)
    


    