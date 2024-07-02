from   DDDAPI.Include.API.COMMON.Domain.valueObjects.Value_object import ValueObject

class Plato_Nombre_VO(ValueObject):
    
    nombre:str;

    def __init__(self, nombre):
        nombre = Plato_Nombre_VO.equals(nombre)
        if nombre is None:
            raise ValueError("El nombre no puede ser vacio")
        super().__init__()
        self.nombre = nombre

    def equals(self, other: 'Plato_Nombre_VO') -> bool:
        return self.nombre == other.nombre
    
    def valid(self) -> bool:
        return len(self.nombre) > 0
    
    def get_nombre(self) -> str:
        return self
    
    @staticmethod
    def create(nombre: str) -> 'Plato_Nombre_VO':
        return Plato_Nombre_VO(nombre)
