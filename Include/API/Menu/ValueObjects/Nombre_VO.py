from Include.API.COMMON.Domain.valueObjects import ValueObject

class Nombre_Menu_VO(ValueObject):
    

    def __init__(self, nombre:str):
        nombre = Nombre_Menu_VO.equals(nombre)
        if nombre is None:
            raise ValueError("El nombre no puede ser vacio")
        super().__init__()
        self.nombre = nombre

    def equals(self, other: 'Nombre_Menu_VO') -> bool:
        return self.nombre == other.nombre
    
    def valid(self) -> bool:
        return len(self.nombre) > 0
    
    def get_nombre(self) -> str:
        return self
    
    @staticmethod
    def create(nombre: str) -> 'Nombre_Menu_VO':
        return nombre