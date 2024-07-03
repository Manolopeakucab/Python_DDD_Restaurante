from Include.API.COMMON.Domain.valueObjects import Value_object;

class Nombre_VO(Value_object):

    nombre:str;

    def __init__(self, nombre: str):
        nombre = Nombre_VO.valid(nombre);
        if nombre is None:
            raise ValueError("El nombre no puede ser vacio")
        self._nombre = nombre

    def equals(self, other: 'Nombre_VO') -> bool:
        return self._nombre == other._nombre
    
    def valid(self) -> bool:
        return self._nombre != None
    
    def get_value(self) -> str:
        return self
    
    staticmethod
    def create(nombre: str) -> 'Nombre_VO':
        return Nombre_VO(nombre)